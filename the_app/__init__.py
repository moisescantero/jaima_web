from flask import Flask
from flask_mail import Mail  # 1.mail- Importamos la clase Mail
from flask_login import LoginManager#1.user_login- importamos loginmanager para gestionar usuarios

app = Flask(__name__, instance_relative_config=True)#creamos app y configuramos instancia relativa al fichero config.py
app.config.from_object("_config")#ruta al fichero config.py donde guardamos nuestra SECRET_KEY para evitar phising a nuestra web
mail = Mail()  # 2.mail- Instanciamos un objeto de tipo Mail
mail.init_app(app)  # 3.mail- Inicializamos el objeto mail

#login_manager = LoginManager(app)#2.user_login- instanciar loginmanager


from the_app import routes





