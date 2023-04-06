#!/bin/bash

API_NAME=Update_Steam-Game

# Créer les dossiers
mkdir $API_NAME
cd $API_NAME
mkdir api api/endpoints api/utils tests

# Créer les fichiers
touch README.md requirements.txt app.py config.py
cd api
touch __init__.py
cd endpoints
touch __init__.py endpoint1.py endpoint2.py
cd ..
cd utils
touch __init__.py database.py authentication.py
cd ../..
cd tests
touch __init__.py test_endpoint1.py test_endpoint2.py

# Ajouter du contenu dans les fichiers
echo "# My API" >> README.md
echo "flask" >> requirements.txt
echo "from flask import Flask\n\napp = Flask(__name__)\n\nif __name__ == '__main__':\n    app.run(debug=True)" >> app.py
echo "DATABASE_URI = 'sqlite:///my_database.db'" >> config.py

# Afficher un message pour indiquer que la création est terminée
echo "La structure de l'API a été créée avec succès."
