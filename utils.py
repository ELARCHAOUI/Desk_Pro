
import google.generativeai as genai
import os

def get_llm_insights(ticket_text: str) -> str:
    """
    Utilise l'API Google Gemini pour analyser le texte d'un ticket de support.

    Args:
        ticket_text: Le contenu brut du ticket de support.

    Returns:
        Une chaîne de caractères formatée en Markdown contenant l'analyse,
        ou un message d'erreur si un problème survient.
    """
    
    # --- Étape 1: Configuration de l'API ---

    try:
        api_key = os.environ["GOOGLE_API_KEY"]
        genai.configure(api_key=api_key)
    except KeyError:
        return "ERREUR : La variable d'environnement GOOGLE_API_KEY n'a pas été trouvée."

    # --- Étape 2: Création du Prompt ---

    prompt = f"""
    Tu es un assistant expert pour les agents de support client. Ton ton est professionnel, empathique et efficace.
    
    Voici un nouveau ticket de support client qui vient d'arriver :
    ---
    {ticket_text}
    ---

    Ta mission est de fournir une analyse rapide et structurée pour aider l'agent à traiter ce ticket.
    Génère une réponse en 3 parties distinctes, formatée en Markdown :

    ### 1. Résumé du Problème
    Résume le problème principal du client en une seule phrase concise (maximum 20 mots).

    ### 2. Prochaines Étapes Suggérées
    Propose une liste de 2 ou 3 actions concrètes et numérotées que l'agent devrait entreprendre pour résoudre ce ticket. Sois précis.

    ### 3. Brouillon de Réponse au Client
    Rédige une première réponse courte et polie à envoyer au client. Remercie-le, montre de l'empathie, et informe-le que son problème est en cours de traitement. Ne promets pas de solution immédiate.
    """

    # --- Étape 3: Appel à l'API Gemini ---
    try:
        model = genai.GenerativeModel("gemini-1.5-flash-latest")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        # Gérer les erreurs potentielles de l'API (ex: quota dépassé, problème de connexion)
        return f"Une erreur est survenue lors de l'appel à l'API Gemini : {e}"


if __name__ == "__main__":
    # Créez un exemple de ticket pour tester
    sample_ticket = """
    Bonjour,
    J'ai passé une commande (numéro #12345) la semaine dernière et le suivi indique qu'elle a été livrée,
    mais je n'ai jamais reçu le colis. J'ai vérifié auprès de mes voisins et personne ne l'a vu.
    Pouvez-vous m'aider à localiser mon colis ou à organiser une réexpédition ?
    Merci,
    Jean Dupont
    """
    
    print("--- Test de la fonction get_llm_insights ---")
    analysis = get_llm_insights(sample_ticket)
    print(analysis)