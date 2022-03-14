# Gestionnaire d'albums photos

Picture permet aux utilisateurs de se connecter, de créer et de stocker des albums et des photos pour organiser de précieux souvenirs. S'ils disent qu'une image vaut 1000 mots, alors combien de plus est un album photo ou plusieurs albums photo ?



###Installation

##### A besoin:
*Python 3.10
* Environnement virtuel pour installer les dépendances.

Voir requirements.txt pour les dépendances.

###
`
$ git clone https://github.com/Robert9188/album.git
$ cd picture
$ env\Scripts\activate
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver
http://127.0.0.1:8000/%5Eadmin/login/?next=/%255Eadmin/
admin: admin
password: password

Vous pouvez commencer ! N'hésitez pas à envoyer un message si des problèmes surviennent.

Nous n'avons pas puis effectuer les tests suites au probleme la commande pytest qui refuse de s'installer , malgrer plusieurs recherche et tutos
