from flask import Flask
from flask_mail import Mail  # 1. Importamos la clase Mail

app = Flask(__name__, instance_relative_config=True)#creamos app y configuramos instancia relativa al fichero config.py
app.config.from_object("_config")#ruta al fichero config.py donde guardamos nuestra SECRET_KEY para evitar phising a nuestra web
mail = Mail()  # 2. Instanciamos un objeto de tipo Mail
mail.init_app(app)  # 3. Inicializamos el objeto mail

from the_app import routes





