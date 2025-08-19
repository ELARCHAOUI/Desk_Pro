

import streamlit as st
import pickle
from utils import get_llm_insights 

# --- Configuration de la Page ---
st.set_page_config(
    page_title="ZenDesk Pro Assistant",
    page_icon="⚡️",
    layout="wide"
)

st.sidebar.title("À Propos de ZenDesk Pro")
st.sidebar.info(
    "Ce projet combine un modèle prédictif (LightGBM) pour la catégorisation de tickets "
    "et un LLM (Google Gemini) pour l'analyse et la génération de réponses. "
    "Les données sont gérées via une base de données SQL (SQLite)."
)
st.sidebar.success("Réalisé par : [EL ARCHAOUI](https://www.linkedin.com/in/mohamed-el-archaoui/)")

@st.cache_resource
def load_model():
    """Charge le pipeline de classification depuis le fichier pickle."""
    try:
        with open('ticket_classifier_pipeline.pkl', 'rb') as f:
            pipeline = pickle.load(f)
        return pipeline
    except FileNotFoundError:
        st.error("ERREUR : Le fichier du modèle 'ticket_classifier_pipeline.pkl' est introuvable.")
        st.info("Veuillez d'abord exécuter le notebook 'train_model.ipynb' pour entraîner et sauvegarder le modèle.")
        return None

pipeline = load_model()

# --- Interface Utilisateur ---
st.title("ZenDesk Pro ⚡️ - Assistant d'Analyse de Tickets")
st.markdown("Collez le contenu d'un ticket de support ci-dessous pour obtenir une analyse instantanée.")

st.divider()

# Zone de texte pour la saisie du ticket
ticket_text = st.text_area(
    "Contenu du ticket de support :",
    height=200,
    placeholder="Ex: Bonjour, je n'arrive pas à me connecter à mon compte. Mon mot de passe ne semble pas fonctionner..."
)

# Bouton pour lancer l'analyse
if st.button("Analyser le Ticket", type="primary"):
    # --- Logique de Traitement ---
    if not ticket_text.strip():
        st.warning("Veuillez entrer le texte d'un ticket à analyser.")
    elif pipeline is None:
        
        st.stop()
    else:
        with st.spinner("Analyse en cours... Le modèle prédictif et l'IA générative travaillent..."):
            
            # --- 1. Cerveau Prédictif (LightGBM) ---
           
            predicted_category = pipeline.predict([ticket_text])[0]
            
            # --- 2. Cerveau Génératif (LLM) ---
            llm_analysis = get_llm_insights(ticket_text)
            
            st.success("Analyse terminée !")
            st.divider()
            
            # --- Affichage des Résultats ---
            st.subheader("Résultats de l'Analyse Intelligente")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric(label="**Catégorie Prédite**", value=predicted_category)
            
            with col2:
                
                st.markdown(llm_analysis)