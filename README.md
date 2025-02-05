# PIPO_APP
* Dans le dossier 'SIGN', supprimer le sous repertoire '__pycache__'
* Dans le dossier 'SIGN/migrations', supprimer le sous repertoire '__pycache__' et tous les fichiers à l'exception de '__init.py__'
* Ouvrir une invite de commande ou un terminal depuis le repertoire de base du projet
* Taper les commandes:
  * python3 manage.py makemigrations
  * python3 manage.py migrate
  * python3 manage.py createsuperuser --username <username> --email <email> (Entrer ensuite un mot de passe si demandé)
  * python3 manage.py runserver
* Creer a la racine du repertoire 'PIPO_APP/PIPO_APP' un fichier '.env'(sans extension) qui contiendra les lignes suivantes:
  * EMAIL_HOST_USER = une adresse email
  * EMAIL_HOST_PASSWORD = un mot de passe
  * DEFAULT_FROM_EMAIL = une adresse email par defaut
  * SEL = une chaine de caractères et de symboles
