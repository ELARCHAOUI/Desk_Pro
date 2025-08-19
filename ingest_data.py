# ingest_data.py

import pandas as pd
import sqlite3
import os

# --- Configuration ---

CSV_PATH = '../data/complaints.csv'
DB_PATH = '../data/support_tickets.db'    # On garde le même nom pour la base de données
TABLE_NAME = 'tickets'                 # On garde le même nom pour la table

def ingest_data():
    """
    Lit les données du "Consumer Complaint Database", les nettoie,
    et charge un échantillon dans une base de données SQLite.
    """
    
    # --- Étape 1: Vérifier si le fichier CSV existe ---
    if not os.path.exists(CSV_PATH):
        print(f"ERREUR : Le fichier {CSV_PATH} n'a pas été trouvé.")
        print("Veuillez télécharger le dataset 'complaints.csv' et le placer dans le dossier 'data/'.")
        return

    print(f"Lecture du fichier CSV depuis : {CSV_PATH}")
    try:
        # Lire le CSV. Certains fichiers peuvent avoir des problèmes d'encodage.
        # 'latin-1' est souvent une bonne solution de repli.
        df = pd.read_csv(CSV_PATH, encoding='latin-1')
    except Exception as e:
        print(f"Une erreur est survenue lors de la lecture du CSV : {e}")
        return

    # --- Étape 2: Sélectionner, renommer et nettoyer les colonnes ---
    print("Nettoyage et sélection des données...")
    
    # Définir les colonnes qui nous intéressent et leurs nouveaux noms
    colonnes_a_garder = {
        'Consumer complaint narrative': 'description', # Le texte de la plainte
        'Product': 'category'                     # La catégorie que l'on veut prédire
    }
    
    # Vérifier si les colonnes nécessaires existent
    if not all(col in df.columns for col in colonnes_a_garder.keys()):
        print("ERREUR : Les colonnes requises ('Consumer complaint narrative', 'Product') ne sont pas toutes présentes.")
        return
        
    # Garder uniquement les colonnes sélectionnées
    df_selection = df[list(colonnes_a_garder.keys())]
    
    # Renommer les colonnes pour avoir des noms simples
    df_renamed = df_selection.rename(columns=colonnes_a_garder)
    
    # Étape cruciale : supprimer les lignes où il n'y a pas de description textuelle
    df_cleaned = df_renamed.dropna(subset=['description'])
    
    print(f"Nombre de tickets avec description : {len(df_cleaned)}")

    # --- Étape 3: Prendre un échantillon pour accélérer le projet ---
    # Le dataset est très grand. Travailler sur un échantillon est plus rapide.
    # 20 000 est un bon nombre pour un projet de portfolio.
    if len(df_cleaned) > 20000:
        print("Prise d'un échantillon aléatoire de 20 000 tickets...")
        df_sample = df_cleaned.sample(n=20000, random_state=42)
    else:
        df_sample = df_cleaned
        
    print(f"Taille finale de l'échantillon : {len(df_sample)}")
    print("Aperçu des données finales :")
    print(df_sample.head())

    # --- Étape 4: Connexion et chargement dans SQLite ---
    print(f"Connexion à la base de données SQLite à : {DB_PATH}")
    conn = sqlite3.connect(DB_PATH)
    
    print(f"Chargement des données dans la table '{TABLE_NAME}'...")
    try:
        df_sample.to_sql(TABLE_NAME, conn, if_exists='replace', index=False)
        print("Les données ont été chargées avec succès dans la base de données.")
    except Exception as e:
        print(f"Une erreur est survenue lors du chargement des données dans SQL : {e}")
    finally:
        conn.close()
        print("Connexion à la base de données fermée.")

# --- Point d'entrée du script ---
if __name__ == "__main__":
    ingest_data()