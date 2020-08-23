from the_app import app
from flask import render_template


@app.route("/")
def index():
    return render_template("base.html")

@app.route("/about_us")
def about_us():
    return render_template("about_us.html")    

@app.route("/about_angel")
def about_angel():
    return render_template("about_angel.html")

@app.route("/about_exposition")
def about_exposition():
    return render_template("about_exposition.html")   

@app.route("/about_clothing_store")
def about_clothing_store():
    return render_template("about_clothing_store.html")   

@app.route("/rents")
def rents():
    return render_template("rents.html")

@app.route("/rents_boatos")
def rents_boatos():
    return render_template("rents_boatos.html")

@app.route("/rents_040913_boato_marron")
def rents_040913_boato_marron():
    return render_template("rents_040913_boato_marron.html")

@app.route("/rents_040015_boato_blanco")
def rents_040015_boato_blanco():
    return render_template("rents_040015_boato_blanco.html")

@app.route("/rents_040016_boato_rojo")
def rents_040016_boato_rojo():
    return render_template("rents_040016_boato_rojo.html")

@app.route("/rents_040014_boato_lila")
def rents_040014_boato_lila():
    return render_template("rents_040014_boato_lila.html")

@app.route("/rents_040310_boato_zegries")
def rents_040310_boato_zegries():
    return render_template("rents_040310_boato_zegries.html")

@app.route("/rents_040207_boato_tuareg")
def rents_040207_boato_tuareg():
    return render_template("rents_040207_boato_tuareg.html")

@app.route("/rents_040807_boato_azul_beduinas")
def rents_040807_boato_azul_beduinas():
    return render_template("rents_040807_boato_azul_beduinas.html")

@app.route("/rents_040006_boato_amarillo")
def rents_040006_boato_amarillo():
    return render_template("rents_040006_boato_amarillo.html")

@app.route("/rents_040020_boato_altea")
def rents_040020_boato_altea():
    return render_template("rents_040020_boato_altea.html")

@app.route("/rents_040705_boato_jeque")
def rents_040705_boato_jeque():
    return render_template("rents_040705_boato_jeque.html")

@app.route("/rents_040008_boato_rojo_dorado")
def rents_040008_boato_rojo_dorado():
    return render_template("rents_040008_boato_rojo_dorado.html")


@app.route("/sales")
def sales():
    return render_template("sales.html")

@app.route("/actuality")
def actuality():
    return render_template("actuality.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/my_jaima")
def my_jaima():
    return render_template("my_jaima.html")
