# Desk_Pro : Assistant d'Analyse de Tickets de Support

##  Le Problème

Les équipes de support client sont souvent submergées par un grand volume de tickets. Le tri manuel, la compréhension du problème, et la rédaction des premières réponses sont des tâches répétitives et chronophages qui ralentissent la résolution des problèmes.

##  La Solution : Desk Pro

ZenDesk Pro est un outil intelligent conçu pour augmenter l'efficacité des agents de support. En collant simplement le texte d'un ticket, l'agent obtient instantanément :
1.  **Une Catégorisation Automatique :** Le ticket est classé dans la bonne catégorie (ex: "Debt collection", "Student loan") grâce à un modèle prédictif.
2.  **Une Analyse par IA Générative :** Un LLM fournit un résumé concis du problème, des suggestions d'actions et un brouillon de réponse à envoyer au client.

##  Architecture et Compétences

Ce projet met en œuvre un pipeline de Data Science complet, de la gestion des données à la mise en production d'un modèle.

**Pipeline de Données :**
`CSV brut` ➔ `Script d'ingestion Python (Pandas)` ➔ `Base de données structurée (SQLite)`

**Pipeline de Machine Learning :**
`Requête SQL` ➔ `Vectorisation de texte (TF-IDF)` ➔ `Entraînement de modèle (LightGBM)` ➔ `Sauvegarde du modèle (Pickle)`

**Pipeline de l'Application :**
`Interface Streamlit` ➔ `Modèle prédictif (LightGBM)` + `Modèle génératif (Google Gemini)` ➔ `Affichage des résultats`

### Compétences Mises en Œuvre
*   **Gestion de Données :** SQL (SQLite), Python (Pandas) pour l'ingestion et la manipulation de données.
*   **Machine Learning Prédictif :** Scikit-learn, LightGBM pour la classification de texte.
*   **NLP :** Feature Engineering avec TF-IDF.
*   **IA Générative :** Intégration d'un LLM (Google Gemini) via API, Prompt Engineering.
*   **Développement :** Création d'une application web interactive avec Streamlit.

##  Installation et Utilisation

### Prérequis
*   Python 3.9 ou supérieur
*   Une clé API Google Gemini


##  Contact

[EL ARCHAOUI] - (https://www.linkedin.com/in/mohamed-el-archaoui/)
