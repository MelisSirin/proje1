from flask import Flask,render_template

app = Flask(__name__)

@app.route('/yazar/<string:id>')
def yazar(id):
   return "Kitap ID si:" + id

# melisin iletisim Sayfası
@app.route('/iletisim')
def iletisim():
   return render_template("iletisim.html")

# Hakkımızda Sayfası
@app.route('/adres')
def adres():
    id = 6
    return render_template("adres.html", sayfabasligi="", sayfaid = id)




# resim-malzemesi-satisi Sayfası
@app.route('/resim-malzemesi-satisi')
def resim_malzemesi_satisi():
    return render_template("resim-malzemesi-satisi.html")


if __name__ == "__main__":
    app.run(debug=True)