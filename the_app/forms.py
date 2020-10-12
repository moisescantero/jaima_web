

from flask_wtf import FlaskForm, Form#clase básica del formulario para heredar campos, tipo de campos, validaciones, etc
from wtforms import StringField, FloatField, SubmitField, HiddenField, SelectField, FileField, DecimalField, TextAreaField#importar de wtforms los campos del formulario que queramos heredar
from wtforms.validators import DataRequired, Length, ValidationError#importar de wtforms los validadores del formulario que queremos heredar
from flask_wtf.file import FileAllowed



def validate_phone(form, field):#valida teléfono móvil
    if Length(field.data) != 9:
        raise ValidationError("El teléfono móvil debe contener 9 números.")

def validate_email(form, field):#valida que el campo tenga valores.
    for i in field.data:
        if i != "@":
            raise ValidationError("Debe introducir un correo electrónico válido.")
        



class ContactForm(FlaskForm):
    id = HiddenField('id')
    
    user_name = StringField("Nombre completo(*): ", validators=[DataRequired(message="Este campo no puede estar vacío.")])#campo para nombre completo definido como string y con validadores
    user_email = StringField("Correo electrónico(*): ", validators=[DataRequired(message="Este campo no puede estar vacío."), validate_email])#campo para correo eléctronico definido como string y con validadores
    phone = DecimalField("Teléfono móvil(*): ", places=9, validators=[DataRequired(message="Este campo no puede estar vacío."), validate_phone])#campo para nombre completo definido como string y con validadores
    message = TextAreaField("Mensaje: ", validators=[DataRequired(message="Indique brevemente su consulta.")])

    accept_button = SubmitField("Enviar")
    
    need_input = StringField("(*) Campos necesarios.")


class CreatingForm(FlaskForm):
    id = HiddenField('id')
    
    title_post = StringField("Título del post(*): ", validators=[DataRequired(message="Este campo no puede estar vacío.")])#campo para title_post definido como string y con validadores
    body_post = TextAreaField("Cuerpo del post(*): ", validators=[DataRequired(message="Este campo no puede estar vacío.")])#campo para body_post definido como string y con validadores
    image_post = FileField('Imagen del post: ', validators=[FileAllowed(['jpg', 'png'], 'Solo se permiten imágenes')])#campo archivo para image_post con archivos permitidos y mensaje de error
    
    accept_button_post = SubmitField("Enviar")
    
    need_input = StringField("(*) Campos necesarios.")