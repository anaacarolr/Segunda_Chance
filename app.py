from datetime import datetime
from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

@app.route('/')
def index():
    return redirect(url_for("home"))

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/adocao')
def adocao():
    return render_template("adotar.html")

@app.route('/denuncia')
def denuncia():
    return render_template("denuncia.html")

@app.route('/ongs')
def ongs():
    return render_template("ongs.html")

@app.route('/cadastro')
def cadastro():
    return render_template("cadastro.html")

@app.route('/cadastro_ong')
def cadastro_ong():
    return render_template("cadastro_ong.html")


if __name__ == '__main__':
    app.run(debug=True, port=5003, host='0.0.0.0')
