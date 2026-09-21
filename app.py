from datetime import datetime
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_login import LoginManager, UserMixin

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

@app.route('/denuncia_anonima')
def denuncia_anonima():
    return render_template("denuncia_anonima.html")

@app.route('/ongs')
def ongs():
    return render_template("ongs.html")

@app.route('/cadastro')
def cadastro():
    return render_template("cadastro.html")

@app.route('/cadastro_ong')
def cadastro_ong():
    print("Cadastro de ong")
    return render_template("cadastro_ong.html")

@app.route('/cadastro_animal')
def cadastro_animal():
    return render_template("cadastro_animal.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/login_ong')
def login_ong():
    return render_template("login_ong.html")

@app.route('/ver_denuncias')
def ver_denuncias():
    return render_template("ver_denuncias.html")

if __name__ == '__main__':
    app.run(debug=True, port=5030, host='0.0.0.0')
