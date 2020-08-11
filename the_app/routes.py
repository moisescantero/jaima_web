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
