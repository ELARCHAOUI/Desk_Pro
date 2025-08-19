

import pickle

print("Tentative de chargement du pipeline depuis 'ticket_classifier_pipeline.pkl'...")
try:
    with open('ticket_classifier_pipeline.pkl', 'rb') as f:
        pipeline = pickle.load(f)
    print("Chargement réussi !")
    
    print("\nTentative de prédiction sur un exemple de texte...")
    sample_text = ["My credit card payment is late."]
    prediction = pipeline.predict(sample_text)
    
    print(f"\nPrédiction réussie ! Catégorie prédite : {prediction[0]}")
    print("\nCONCLUSION : Votre fichier .pkl est VALIDE.")
    
except Exception as e:
    print("\nERREUR : Le test a échoué.")
    print(f"L'erreur est : {e}")
    print("\nCONCLUSION : Votre fichier .pkl est INVALIDE. Le problème vient du notebook 'train_model.ipynb'.")