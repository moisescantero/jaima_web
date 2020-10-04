

from flask_wtf import FlaskForm, Form#clase básica del formulario para heredar campos, tipo de campos, validaciones, etc
from wtforms import StringField, FloatField, SubmitField, HiddenField, SelectField, Field, DecimalField#importar de wtforms los campos del formulario que queramos heredar
from wtforms.validators import DataRequired, Length, ValidationError#importar de wtforms los validadores del formulario que queremos heredar



def validate_phone(form, field):#valida teléfono móvil
    if Length(field.data) != 9:
        raise ValidationError("El teléfono móvil debe contener 9 números.")

def validate_email(form, field):#valida que el campo tenga valores.
    for i in field.data:
        if i != "@":
            raise ValidationError("Debe introducir un correo electrónico válido.")
        



class ContactForm(FlaskForm):
    id = HiddenField('id')
    
    user_name = StringField("Nombre completo: ", validators=[DataRequired(message="Este campo no puede estar vacío.")])#campo para nombre completo definido como string y con validadores
    user_email = StringField("Correo electrónico: ", validators=[DataRequired(message="Este campo no puede estar vacío."), validate_email])#campo para correo eléctronico definido como string y con validadores
    phone = DecimalField("Teléfono móvil: ", places=9, validators=[DataRequired(message="Este campo no puede estar vacío."), validate_phone])#campo para nombre completo definido como string y con validadores
    message = StringField("Mensaje: ", validators=[DataRequired(message="Indique brevemente su consulta.")])

    accept_button = SubmitField("Enviar")
    cancel_button = SubmitField("Cancelar")