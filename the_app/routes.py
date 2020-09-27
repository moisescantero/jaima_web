from the_app import app
from flask import render_template


@app.route("/")
def index():
    return render_template("base.html")


#rutas para apartado sobre nosotros
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


#rutas para alquileres de boatos
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


#rutas para alquileres de capitanes
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


#rutas para alquileres escuadras masculinas
@app.route("/rents_men")
def rents_men():
    return render_template("rents_men.html")
@app.route("/rents_011020_hombre_guerrero")
def rents_011020_hombre_guerrero():
    return render_template("rents_011020_hombre_guerrero.html")
@app.route("/rents_010119_hombre_abencerraje")
def rents_010119_hombre_abencerraje():
    return render_template("rents_010119_hombre_abencerraje.html")
@app.route("/rents_010419_hombre_jenizaro")
def rents_010419_hombre_jenizaro():
    return render_template("rents_010419_hombre_jenizaro.html")
@app.route("/rents_010219_hombre_tuareg")
def rents_010219_hombre_tuareg():
    return render_template("rents_010219_hombre_tuareg.html")
@app.route("/rents_010218_hombre_tuareg")
def rents_010218_hombre_tuareg():
    return render_template("rents_010218_hombre_tuareg.html")
@app.route("/rents_010318_hombre_caiman")
def rents_010318_hombre_caiman():
    return render_template("rents_010318_hombre_caiman.html")
@app.route("/rents_010518_hombre_ecuador")
def rents_010518_hombre_ecuador():
    return render_template("rents_010518_hombre_ecuador.html")
@app.route("/rents_010118_hombre_abencerraje")
def rents_010118_hombre_abencerraje():
    return render_template("rents_010118_hombre_abencerraje.html")
@app.route("/rents_011018_hombre_guerrero")
def rents_011018_hombre_guerrero():
    return render_template("rents_011018_hombre_guerrero.html")
@app.route("/rents_011117_hombre_dragon")
def rents_011117_hombre_dragon():
    return render_template("rents_011117_hombre_dragon.html")
@app.route("/rents_010117_hombre_abencerraje")
def rents_010117_hombre_abencerraje():
    return render_template("rents_010117_hombre_abencerraje.html")
@app.route("/rents_010217_hombre_tuareg")
def rents_010217_hombre_tuareg():
    return render_template("rents_010217_hombre_tuareg.html")
@app.route("/rents_010416_hombre_jenizaro")
def rents_010416_hombre_jenizaro():
    return render_template("rents_010416_hombre_jenizaro.html")
@app.route("/rents_010216_hombre_tuareg")
def rents_010216_hombre_tuareg():
    return render_template("rents_010216_hombre_tuareg.html")
@app.route("/rents_010116_hombre_abencerraje")
def rents_010116_hombre_abencerraje():
    return render_template("rents_010116_hombre_abencerraje.html")
@app.route("/rents_010316_hombre_caiman")
def rents_010316_hombre_caiman():
    return render_template("rents_010316_hombre_caiman.html")
@app.route("/rents_010516_hombre_ecuador")
def rents_010516_hombre_ecuador():
    return render_template("rents_010516_hombre_ecuador.html")
@app.route("/rents_010115_hombre_abencerraje")
def rents_010115_hombre_abencerraje():
    return render_template("rents_010115_hombre_abencerraje.html")
@app.route("/rents_010515_hombre_ecuador")
def rents_010515_hombre_ecuador():
    return render_template("rents_010515_hombre_ecuador.html")
@app.route("/rents_010215_hombre_tuareg")
def rents_010215_hombre_tuareg():
    return render_template("rents_010215_hombre_tuareg.html")
@app.route("/rents_011015_hombre_guerrero")
def rents_011015_hombre_guerrero():
    return render_template("rents_011015_hombre_guerrero.html")
@app.route("/rents_011014_hombre_guerrero")
def rents_011014_hombre_guerrero():
    return render_template("rents_011014_hombre_guerrero.html")
@app.route("/rents_010214_hombre_tuareg")
def rents_010214_hombre_tuareg():
    return render_template("rents_010214_hombre_tuareg.html")
@app.route("/rents_010414_hombre_jenizaro")
def rents_010414_hombre_jenizaro():
    return render_template("rents_010414_hombre_jenizaro.html")
@app.route("/rents_010514_hombre_ecuador")
def rents_010514_hombre_ecuador():
    return render_template("rents_010514_hombre_ecuador.html")
@app.route("/rents_010913_hombre_ibi")
def rents_010913_hombre_ibi():
    return render_template("rents_010913_hombre_ibi.html")
@app.route("/rents_010413_hombre_jenizaro")
def rents_010413_hombre_jenizaro():
    return render_template("rents_010413_hombre_jenizaro.html")
@app.route("/rents_010213_hombre_tuareg")
def rents_010213_hombre_tuareg():
    return render_template("rents_010213_hombre_tuareg.html")
@app.route("/rents_010312_hombre_zegrie")
def rents_010312_hombre_zegrie():
    return render_template("rents_010312_hombre_zegrie.html")
@app.route("/rents_010112_hombre_abencerraje")
def rents_010112_hombre_abencerraje():
    return render_template("rents_010112_hombre_abencerraje.html")
@app.route("/rents_010212_hombre_tuareg")
def rents_010212_hombre_tuareg():
    return render_template("rents_010212_hombre_tuareg.html")
@app.route("/rents_010211_hombre_tuareg")
def rents_010211_hombre_tuareg():
    return render_template("rents_010211_hombre_tuareg.html")
@app.route("/rents_010411_hombre_jenizaro")
def rents_010411_hombre_jenizaro():
    return render_template("rents_010411_hombre_jenizaro.html")
@app.route("/rents_010111_hombre_abencerraje")
def rents_010111_hombre_abencerraje():
    return render_template("rents_010111_hombre_abencerraje.html")
@app.route("/rents_010611_hombre_sarraceno")
def rents_010611_hombre_sarraceno():
    return render_template("rents_010611_hombre_sarraceno.html")
@app.route("/rents_010511_hombre_ecuador")
def rents_010511_hombre_ecuador():
    return render_template("rents_010511_hombre_ecuador.html")
@app.route("/rents_010310_hombre_zegrie")
def rents_010310_hombre_zegrie():
    return render_template("rents_010310_hombre_zegrie.html")
@app.route("/rents_010110_hombre_abencerraje")
def rents_010110_hombre_abencerraje():
    return render_template("rents_010110_hombre_abencerraje.html")
@app.route("/rents_010510_hombre_ecuador")
def rents_010510_hombre_ecuador():
    return render_template("rents_010510_hombre_ecuador.html")
@app.route("/rents_010109_hombre_abencerraje")
def rents_010109_hombre_abencerraje():
    return render_template("rents_010109_hombre_abencerraje.html")
@app.route("/rents_010609_hombre_sarraceno")
def rents_010609_hombre_sarraceno():
    return render_template("rents_010609_hombre_sarraceno.html")
@app.route("/rents_010409_hombre_jenizaro")
def rents_010409_hombre_jenizaro():
    return render_template("rents_010409_hombre_jenizaro.html")
@app.route("/rents_010509_hombre_ecuador")
def rents_010509_hombre_ecuador():
    return render_template("rents_010509_hombre_ecuador.html")
@app.route("/rents_010209_hombre_tuareg")
def rents_010209_hombre_tuareg():
    return render_template("rents_010209_hombre_tuareg.html")
@app.route("/rents_010709_hombre_jeque")
def rents_010709_hombre_jeque():
    return render_template("rents_010709_hombre_jeque.html")
@app.route("/rents_010608_hombre_sarraceno")
def rents_010608_hombre_sarraceno():
    return render_template("rents_010608_hombre_sarraceno.html")
@app.route("/rents_010408_hombre_jenizaro")
def rents_010408_hombre_jenizaro():
    return render_template("rents_010408_hombre_jenizaro.html")
@app.route("/rents_010108_hombre_abencerraje")
def rents_010108_hombre_abencerraje():
    return render_template("rents_010108_hombre_abencerraje.html")
@app.route("/rents_010206_hombre_tuareg")
def rents_010206_hombre_tuareg():
    return render_template("rents_010206_hombre_tuareg.html")
@app.route("/rents_010606_hombre_sarraceno")
def rents_010606_hombre_sarraceno():
    return render_template("rents_010606_hombre_sarraceno.html")

#rutas para alquileres escuadras femeninas
@app.route("/rents_women")
def rents_women():
    return render_template("rents_women.html")
@app.route("/rents_020519_mujer_ecuador")
def rents_020519_mujer_ecuador():
    return render_template("rents_020519_mujer_ecuador.html")
@app.route("/rents_020219_mujer_tuaresa")
def rents_020219_mujer_tuaresa():
    return render_template("rents_020219_mujer_tuaresa.html")
@app.route("/rents_021020_mujer_guerrera")
def rents_021020_mujer_guerrera():
    return render_template("rents_021020_mujer_guerrera.html")
@app.route("/rents_020819_mujer_beduina")
def rents_020819_mujer_beduina():
    return render_template("rents_020819_mujer_beduina.html")
@app.route("/rents_020419_mujer_jenizara")
def rents_020419_mujer_jenizara():
    return render_template("rents_020419_mujer_jenizara.html")
@app.route("/rents_020319_mujer_zegrie")
def rents_020319_mujer_zegrie():
    return render_template("rents_020319_mujer_zegrie.html")
@app.route("/rents_020318_mujer_zegrie")
def rents_020318_mujer_zegrie():
    return render_template("rents_020318_mujer_zegrie.html")
@app.route("/rents_020218_mujer_tuaresa")
def rents_020218_mujer_tuaresa():
    return render_template("rents_020218_mujer_tuaresa.html")
@app.route("/rents_020518_mujer_ecuador")
def rents_020518_mujer_ecuador():
    return render_template("rents_020518_mujer_ecuador.html")
@app.route("/rents_020818_mujer_beduina")
def rents_020818_mujer_beduina():
    return render_template("rents_020818_mujer_beduina.html")
@app.route("/rents_021018_mujer_guerrera")
def rents_021018_mujer_guerrera():
    return render_template("rents_021018_mujer_guerrera.html")
@app.route("/rents_021117_mujer_dragona")
def rents_021117_mujer_dragona():
    return render_template("rents_021117_mujer_dragona.html")
@app.route("/rents_020817_mujer_beduina")
def rents_020817_mujer_beduina():
    return render_template("rents_020817_mujer_beduina.html")
@app.route("/rents_020217_mujer_tuaresa")
def rents_020217_mujer_tuaresa():
    return render_template("rents_020217_mujer_tuaresa.html")
@app.route("/rents_020716_mujer_jeque")
def rents_020716_mujer_jeque():
    return render_template("rents_020716_mujer_jeque.html")
@app.route("/rents_020416_mujer_jenízara")
def rents_020416_mujer_jenízara():
    return render_template("rents_020416_mujer_jenízara.html")
@app.route("/rents_020216_mujer_tuaresa")
def rents_020216_mujer_tuaresa():
    return render_template("rents_020216_mujer_tuaresa.html")
@app.route("/rents_020816_mujer_beduina")
def rents_020816_mujer_beduina():
    return render_template("rents_020816_mujer_beduina.html")
@app.route("/rents_020316_mujer_zegrie")
def rents_020316_mujer_zegrie():
    return render_template("rents_020316_mujer_zegrie.html")
@app.route("/rents_020516_mujer_ecuador")
def rents_020516_mujer_ecuador():
    return render_template("rents_020516_mujer_ecuador.html")
@app.route("/rents_020815_mujer_beduina")
def rents_020815_mujer_beduina():
    return render_template("rents_020815_mujer_beduina.html")
@app.route("/rents_020515_mujer_ecuador")
def rents_020515_mujer_ecuador():
    return render_template("rents_020515_mujer_ecuador.html")
@app.route("/rents_021015_mujer_guerrera")
def rents_021015_mujer_guerrera():
    return render_template("rents_021015_mujer_guerrera.html")
@app.route("/rents_021014_mujer_guerrera")
def rents_021014_mujer_guerrera():
    return render_template("rents_021014_mujer_guerrera.html")
@app.route("/rents_020814_mujer_guerrera")
def rents_020814_mujer_guerrera():
    return render_template("rents_020814_mujer_guerrera.html")
@app.route("/rents_020414_mujer_jenizara")
def rents_020414_mujer_jenizara():
    return render_template("rents_020414_mujer_jenizara.html")
@app.route("/rents_020514_mujer_ecuador")
def rents_020514_mujer_ecuador():
    return render_template("rents_020514_mujer_ecuador.html")
@app.route("/rents_020913_mujer_ibi")
def rents_020913_mujer_ibi():
    return render_template("rents_020913_mujer_ibi.html")
@app.route("/rents_020413_mujer_jenizara")
def rents_020413_mujer_jenizara():
    return render_template("rents_020413_mujer_jenizara.html")
@app.route("/rents_021013_mujer_guerrera")
def rents_021013_mujer_guerrera():
    return render_template("rents_021013_mujer_guerrera.html")
@app.route("/rents_020513_mujer_ecuador")
def rents_020513_mujer_ecuador():
    return render_template("rents_020513_mujer_ecuador.html")
@app.route("/rents_020313_mujer_zegrie")
def rents_020313_mujer_zegrie():
    return render_template("rents_020313_mujer_zegrie.html")
@app.route("/rents_020312_mujer_zegrie")
def rents_020312_mujer_zegrie():
    return render_template("rents_020312_mujer_zegrie.html")
@app.route("/rents_020812_mujer_beduina")
def rents_020812_mujer_beduina():
    return render_template("rents_020812_mujer_beduina.html")
@app.route("/rents_020212_mujer_tuaresa")
def rents_020212_mujer_tuaresa():
    return render_template("rents_020212_mujer_tuaresa.html")
@app.route("/rents_020211_mujer_tuaresa")
def rents_020211_mujer_tuaresa():
    return render_template("rents_020211_mujer_tuaresa.html")
@app.route("/rents_020411_mujer_jenizara")
def rents_020411_mujer_jenizara():
    return render_template("rents_020411_mujer_jenizara.html")
@app.route("/rents_020811_mujer_beduina")
def rents_020811_mujer_beduina():
    return render_template("rents_020811_mujer_beduina.html")
@app.route("/rents_020611_mujer_sarracena")
def rents_020611_mujer_sarracena():
    return render_template("rents_020611_mujer_sarracena.html")
@app.route("/rents_021011_mujer_guerrera")
def rents_021011_mujer_guerrera():
    return render_template("rents_021011_mujer_guerrera.html")
@app.route("/rents_020511_mujer_ecuador")
def rents_020511_mujer_ecuador():
    return render_template("rents_020511_mujer_ecuador.html")
@app.route("/rents_020310_mujer_zegrie")
def rents_020310_mujer_zegrie():
    return render_template("rents_020310_mujer_zegrie.html")
@app.route("/rents_020810_mujer_beduina")
def rents_020810_mujer_beduina():
    return render_template("rents_020810_mujer_beduina.html")
@app.route("/rents_020510_mujer_ecuador")
def rents_020510_mujer_ecuador():
    return render_template("rents_020510_mujer_ecuador.html")
@app.route("/rents_020809_mujer_beduina")
def rents_020809_mujer_beduina():
    return render_template("rents_020809_mujer_beduina.html")
@app.route("/rents_020609_mujer_sarracena")
def rents_020609_mujer_sarracena():
    return render_template("rents_020609_mujer_sarracena.html")
@app.route("/rents_020409_mujer_jenizara")
def rents_020409_mujer_jenizara():
    return render_template("rents_020409_mujer_jenizara.html")
@app.route("/rents_020509_mujer_ecuador")
def rents_020509_mujer_ecuador():
    return render_template("rents_020509_mujer_ecuador.html")
@app.route("/rents_020209_mujer_tuaresa")
def rents_020209_mujer_tuaresa():
    return render_template("rents_020209_mujer_tuaresa.html")
@app.route("/rents_020709_mujer_jeque")
def rents_020709_mujer_jeque():
    return render_template("rents_020709_mujer_jeque.html")
@app.route("/rents_020608_mujer_sarracena")
def rents_020608_mujer_sarracena():
    return render_template("rents_020608_mujer_sarracena.html")
@app.route("/rents_020408_mujer_jenizara")
def rents_020408_mujer_jenizara():
    return render_template("rents_020408_mujer_jenizara.html")
@app.route("/rents_020206_mujer_tuaresa")
def rents_020206_mujer_tuaresa():
    return render_template("rents_020206_mujer_tuaresa.html")
@app.route("/rents_020606_mujer_sarracena")
def rents_020606_mujer_sarracena():
    return render_template("rents_020606_mujer_sarracena.html")

#rutas para alquileres escuadras infantiles
@app.route("/rents_kids")
def rents_kids():
    return render_template("rents_kids.html")
@app.route("/rents_030818_niños_beduina")
def rents_030818_niños_beduina():
    return render_template("rents_030818_niños_beduina.html")
@app.route("/rents_030817_niños_beduina")
def rents_030817_niños_beduina():
    return render_template("rents_030817_niños_beduina.html")
@app.route("/rents_030816_niños_beduina")
def rents_030816_niños_beduina():
    return render_template("rents_030816_niños_beduina.html")
@app.route("/rents_030815_niños_beduina")
def rents_030815_niños_beduina():
    return render_template("rents_030815_niños_beduina.html")
@app.route("/rents_010512_pollito_ecuador")
def rents_010512_pollito_ecuador():
    return render_template("rents_010512_pollito_ecuador.html")
@app.route("/rents_020512_pollita_ecuador")
def rents_020512_pollita_ecuador():
    return render_template("rents_020512_pollita_ecuador.html")
@app.route("/rents_030716_niñas_naranjas")
def rents_030716_niñas_naranjas():
    return render_template("rents_030716_niñas_naranjas.html")
@app.route("/rents_030515_niños_ecuador")
def rents_030515_niños_ecuador():
    return render_template("rents_030515_niños_ecuador.html")
@app.route("/rents_030814_niños_beduina")
def rents_030814_niños_beduina():
    return render_template("rents_030814_niños_beduina.html")
@app.route("/rents_030913_niños_ibi")
def rents_030913_niños_ibi():
    return render_template("rents_030913_niños_ibi.html")
@app.route("/rents_030413_niños_jenizaros")
def rents_030413_niños_jenizaros():
    return render_template("rents_030413_niños_jenizaros.html")
@app.route("/rents_030812_niños_beduina")
def rents_030812_niños_beduina():
    return render_template("rents_030812_niños_beduina.html")
@app.route("/rents_030312_niños_zegrie")
def rents_030312_niños_zegrie():
    return render_template("rents_030312_niños_zegrie.html")
@app.route("/rents_030611_niños_sarraceno")
def rents_030611_niños_sarraceno():
    return render_template("rents_030611_niños_sarraceno.html")
@app.route("/rents_030811_niños_beduina")
def rents_030811_niños_beduina():
    return render_template("rents_030811_niños_beduina.html")
@app.route("/rents_030211_niños_tuareg")
def rents_030211_niños_tuareg():
    return render_template("rents_030211_niños_tuareg.html")
@app.route("/rents_030810_niños_beduina")
def rents_030810_niños_beduina():
    return render_template("rents_030810_niños_beduina.html")
@app.route("/rents_030310_niños_zegrie")
def rents_030310_niños_zegrie():
    return render_template("rents_030310_niños_zegrie.html")
@app.route("/rents_030511_niños_ecuador")
def rents_030511_niños_ecuador():
    return render_template("rents_030511_niños_ecuador.html")
@app.route("/rents_030809_niños_beduina")
def rents_030809_niños_beduina():
    return render_template("rents_030809_niños_beduina.html")
@app.route("/rents_030209_niños_tuareg")
def rents_030209_niños_tuareg():
    return render_template("rents_030209_niños_tuareg.html")
@app.route("/rents_030608_niños_sarraceno")
def rents_030608_niños_sarraceno():
    return render_template("rents_030608_niños_sarraceno.html")
@app.route("/rents_030808_niños_beduina")
def rents_030808_niños_beduina():
    return render_template("rents_030808_niños_beduina.html")
@app.route("/rents_030408_niños_jenizaros")
def rents_030408_niños_jenizaros():
    return render_template("rents_030408_niños_jenizaros.html")
@app.route("/rents_030807_niños_beduina")
def rents_030807_niños_beduina():
    return render_template("rents_030807_niños_beduina.html")

#rutas para alquileres reyes magos
@app.route("/rents_reyes_magos")
def rents_reyes_magos():
    return render_template("rents_reyes_magos.html")
@app.route("/rents_070101_rey_mago")
def rents_070101_rey_mago():
    return render_template("rents_070101_rey_mago.html")
@app.route("/rents_070102_rey_mago")
def rents_070102_rey_mago():
    return render_template("rents_070102_rey_mago.html")
@app.route("/rents_070103_rey_mago")
def rents_070103_rey_mago():
    return render_template("rents_070103_rey_mago.html")
@app.route("/rents_070201_rey_mago")
def rents_070201_rey_mago():
    return render_template("rents_070201_rey_mago.html")
@app.route("/rents_070202_rey_mago")
def rents_070202_rey_mago():
    return render_template("rents_070202_rey_mago.html")
@app.route("/rents_070203_rey_mago")
def rents_070203_rey_mago():
    return render_template("rents_070203_rey_mago.html")
@app.route("/rents_070204_rey_mago")
def rents_070204_rey_mago():
    return render_template("rents_070204_rey_mago.html")
@app.route("/rents_070205_rey_mago")
def rents_070205_rey_mago():
    return render_template("rents_070205_rey_mago.html")
@app.route("/rents_070206_rey_mago")
def rents_070206_rey_mago():
    return render_template("rents_070206_rey_mago.html")
@app.route("/rents_070207_rey_mago")
def rents_070207_rey_mago():
    return render_template("rents_070207_rey_mago.html")
@app.route("/rents_070208_rey_mago")
def rents_070208_rey_mago():
    return render_template("rents_070208_rey_mago.html")
@app.route("/rents_070209_rey_mago")
def rents_070209_rey_mago():
    return render_template("rents_070209_rey_mago.html")
@app.route("/rents_070301_rey_mago")
def rents_070301_rey_mago():
    return render_template("rents_070301_rey_mago.html")
@app.route("/rents_070302_rey_mago")
def rents_070302_rey_mago():
    return render_template("rents_070302_rey_mago.html")
@app.route("/rents_070303_rey_mago")
def rents_070303_rey_mago():
    return render_template("rents_070303_rey_mago.html")
@app.route("/rents_070304_rey_mago")
def rents_070304_rey_mago():
    return render_template("rents_070304_rey_mago.html")
@app.route("/rents_070305_rey_mago")
def rents_070305_rey_mago():
    return render_template("rents_070305_rey_mago.html")
@app.route("/rents_070306_rey_mago")
def rents_070306_rey_mago():
    return render_template("rents_070306_rey_mago.html")
@app.route("/rents_070307_rey_mago")
def rents_070307_rey_mago():
    return render_template("rents_070307_rey_mago.html")
@app.route("/rents_070308_rey_mago")
def rents_070308_rey_mago():
    return render_template("rents_070308_rey_mago.html")
@app.route("/rents_070309_rey_mago")
def rents_070309_rey_mago():
    return render_template("rents_070309_rey_mago.html")
@app.route("/rents_070310_rey_mago")
def rents_070310_rey_mago():
    return render_template("rents_070310_rey_mago.html")
@app.route("/rents_070311_rey_mago")
def rents_070311_rey_mago():
    return render_template("rents_070311_rey_mago.html")
@app.route("/rents_070312_rey_mago")
def rents_070312_rey_mago():
    return render_template("rents_070312_rey_mago.html")
@app.route("/rents_070313_rey_mago")
def rents_070313_rey_mago():
    return render_template("rents_070313_rey_mago.html")
@app.route("/rents_070314_rey_mago")
def rents_070314_rey_mago():
    return render_template("rents_070314_rey_mago.html")
@app.route("/rents_070315_rey_mago")
def rents_070315_rey_mago():
    return render_template("rents_070315_rey_mago.html")
@app.route("/rents_070316_rey_mago")
def rents_070316_rey_mago():
    return render_template("rents_070316_rey_mago.html")
@app.route("/rents_070317_rey_mago")
def rents_070317_rey_mago():
    return render_template("rents_070317_rey_mago.html")
@app.route("/rents_070318_rey_mago")
def rents_070318_rey_mago():
    return render_template("rents_070318_rey_mago.html")
@app.route("/rents_070319_rey_mago")
def rents_070319_rey_mago():
    return render_template("rents_070319_rey_mago.html")
@app.route("/rents_070320_rey_mago")
def rents_070320_rey_mago():
    return render_template("rents_070320_rey_mago.html")
@app.route("/rents_070321_rey_mago")
def rents_070321_rey_mago():
    return render_template("rents_070321_rey_mago.html")


















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
