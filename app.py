# Importation des modules nécessaires depuis Flask
from flask import Flask, request

# Création de l'application Flask
app = Flask(__name__)

# Définition de la route pour traiter les données du formulaire
@app.route('/submit' , methods=['POST' , 'GET'])
def submit():
    # Récupération des données du formulaire
    name = request.form.get('name')
    number = request.form.get('number')
    number2 = request.form.get('number2')
    number3 = request.form.get('number3')
    difficulty = request.form.get('difficulty')
    ingredients = request.form.get('ingredients')
    instructions = request.form.get('instructions')
    notes = request.form.get('notes')
    
    recipe = request.form.get('recipe')
    email = request.form.get('email')
   
    #print(f"Nom: {name} ,Email: {email}")

    # Ici, vous pouvez ajouter le traitement des données
    # Par exemple, enregistrer dans une base de données ou envoyer un email

    # Retourner un message directement à l'utilisateur
    return f"<h1>Merci {name} !</h1><p>Nous avons bien reçu votre message.</p>"
@app.route('/')
def home ():
    return "serveur fonctione"
# Point d'entrée de l'application
if __name__ == '__main__':
    # Démarrage du serveur Flask en mode debug
    app.run(debug=True)