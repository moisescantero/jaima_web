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

@app.route("/rents_captains")
def rents_captains():
    return render_template("rents_captains.html")

@app.route("/rents_012019_capitan_beig_rosa")
def rents_012019_capitan_beig_rosa():
    return render_template("rents_012019_capitan_beig_rosa.html")

@app.route("/rents_022019_capitana_beig_rosa")
def rents_022019_capitana_beig_rosa():
    return render_template("rents_022019_capitana_beig_rosa.html")

@app.route("/rents_012018_capitan_azul_plata")
def rents_012018_capitan_azul_plata():
    return render_template("rents_012018_capitan_azul_plata.html")

@app.route("/rents_022018_capitana_azul_plata")
def rents_022018_capitana_azul_plata():
    return render_template("rents_022018_capitana_azul_plata.html")

@app.route("/rents_012016_capitan_rojo_plata")
def rents_012016_capitan_rojo_plata():
    return render_template("rents_012016_capitan_rojo_plata.html")

@app.route("/rents_022016_capitana_rojo_plata")
def rents_022016_capitana_rojo_plata():
    return render_template("rents_022016_capitana_rojo_plata.html")

@app.route("/rents_012015_capitan_blanco_oro")
def rents_012015_capitan_blanco_oro():
    return render_template("rents_012015_capitan_blanco_oro.html")

@app.route("/rents_022015_capitana_blanco_oro")
def rents_022015_capitana_blanco_oro():
    return render_template("rents_022015_capitana_blanco_oro.html")    

@app.route("/rents_012014_capitan_negro_oro")
def rents_012014_capitan_negro_oro():
    return render_template("rents_012014_capitan_negro_oro.html")

@app.route("/rents_022014_capitana_negro_oro")
def rents_022014_capitana_negro_oro():
    return render_template("rents_022014_capitana_negro_oro.html")

@app.route("/rents_012013_capitan_ibi_marron")
def rents_012013_capitan_ibi_marron():
    return render_template("rents_012013_capitan_ibi_marron.html")

@app.route("/rents_022013_capitana_ibi_marron")
def rents_022013_capitana_ibi_marron():
    return render_template("rents_022013_capitana_ibi_marron.html")

@app.route("/rents_012015_capitan_azul_verde")
def rents_012015_capitan_azul_verde():
    return render_template("rents_012015_capitan_azul_verde.html")

@app.route("/rents_022015_capitana_azul_verde")
def rents_022015_capitana_azul_verde():
    return render_template("rents_022015_capitana_azul_verde.html")

@app.route("/rents_012012_capitan_rosa_plata")
def rents_012012_capitan_rosa_plata():
    return render_template("rents_012012_capitan_rosa_plata.html")

@app.route("/rents_022012_capitana_rosa_plata")
def rents_022012_capitana_rosa_plata():
    return render_template("rents_022012_capitana_rosa_plata.html")

@app.route("/rents_012013_capitan_ibi_ecuador")
def rents_012013_capitan_ibi_ecuador():
    return render_template("rents_012013_capitan_ibi_ecuador.html")

@app.route("/rents_022013_capitana_ibi_ecuador")
def rents_022013_capitana_ibi_ecuador():
    return render_template("rents_022013_capitana_ibi_ecuador.html")

@app.route("/rents_012010_capitan_ibi_morado")
def rents_012010_capitan_ibi_morado():
    return render_template("rents_012010_capitan_ibi_morado.html")

@app.route("/rents_022010_capitana_ibi_morado")
def rents_022010_capitana_ibi_morado():
    return render_template("rents_022010_capitana_ibi_morado.html")

@app.route("/rents_012010_capitan_blanco_plata")
def rents_012010_capitan_blanco_plata():
    return render_template("rents_012010_capitan_blanco_plata.html")

@app.route("/rents_022010_capitana_blanco_plata")
def rents_022010_capitana_blanco_plata():
    return render_template("rents_022010_capitana_blanco_plata.html")

@app.route("/rents_012009_capitan_verde_marron")
def rents_012009_capitan_verde_marron():
    return render_template("rents_012009_capitan_verde_marron.html")

@app.route("/rents_022009_capitana_verde_marron")
def rents_022009_capitana_verde_marron():
    return render_template("rents_022009_capitana_verde_marron.html")

@app.route("/rents_012008_capitan_rojo_negro")
def rents_012008_capitan_rojo_negro():
    return render_template("rents_012008_capitan_rojo_negro.html")

@app.route("/rents_022008_capitana_rojo_negro")
def rents_022008_capitana_rojo_negro():
    return render_template("rents_022008_capitana_rojo_negro.html")

@app.route("/rents_012008_capitan_marron")
def rents_012008_capitan_marron():
    return render_template("rents_012008_capitan_marron.html")

@app.route("/rents_022008_capitana_marron")
def rents_022008_capitana_marron():
    return render_template("rents_022008_capitana_marron.html")

@app.route("/rents_012007_capitan_azul_blanco")
def rents_012007_capitan_azul_blanco():
    return render_template("rents_012007_capitan_azul_blanco.html")

@app.route("/rents_022007_capitana_azul_blanco")
def rents_022007_capitana_azul_blanco():
    return render_template("rents_022007_capitana_azul_blanco.html")

@app.route("/rents_022006_capitana_rojo_beig")
def rents_022006_capitana_rojo_beig():
    return render_template("rents_022006_capitana_rojo_beig.html")


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
