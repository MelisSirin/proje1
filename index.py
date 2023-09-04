from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def anaSayfa():
    return "Merhaba Melis Blog ziyaretçileri!"

@app.route("/ietisim")
def iletisim():
    return """
    <p> kedi muzik ders deniz oyun yemek is
    kesmek uzun goz kisa </p>"""

@app.route("/hobiler")
def hobier():
    return "<h1>resim cizmek</h1>\
<a href='https://www.w3schools.com/'>Visit W3Schools.com!</a>\
<a href='https://www.google.com/'>Visit google!</a>"

@app.route("/adres")
def adres():
    return "kuzukoy 7890w3"


if __name__ == "__main__":
    app.run(debug=True)
