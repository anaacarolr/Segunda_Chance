from flask import Flask, request, render_template, flash, redirect, url_for
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from routes.routes import post_login_usuario, post_usuario, post_ong, post_animal, post_denuncia, get_denuncia, \
    get_categoria, get_animais

app = Flask(__name__)

# Definir a SENHA, em produção colocar em lugar SEGURO
app.config['JWT_SECRET_KEY'] = 'Segund@_ch@nc&'


@app.route('/')
def index():
    return render_template("home.html")

@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/ongs')
def ongs():
    return render_template("ongs.html")


@app.route("/post_usuario", methods=["GET","POST"])
def cadastrar_usuario():
    if request.method == 'POST':
        nome = request.form.get("form-nome")
        email = request.form.get("form-email")
        senha = request.form.get("form-senha")
        resposta = post_usuario(nome=nome, email=email, senha=senha)

        dados_ = resposta
        print(dados_)
        flash(message="Encomenda cadastrada com sucesso")
        return redirect(url_for('listar_animais'))


    return render_template("cadastro.html")


@app.route("/login", methods=["GET", "POST"])
def login_usuarios():
    if request.method == 'POST':
        email = request.form.get("email")
        senha = request.form.get("senha")
        resposta = post_login_usuario(email, senha)

        dados_ = resposta.json()
        print(dados_)
        if resposta.status_code == 200:
            flash(message="Encomenda cadastrada com sucesso")
            return redirect(url_for('listar_animais'))
        else:
            flash(message="Erro ao cadastrar")

    return render_template("login.html")


@app.route("/post_ong", methods=["POST"])
def cadastrar_ong():
    if request.method == 'POST':
        nome = request.form.get("nome")
        cnpj = request.form.get("cnpj")
        estado = request.form.get("estado")
        senha = request.form.get("senha")

        resposta = post_ong(nome, cnpj, estado, senha)

        dados_ = resposta.json()
        print(dados_)
        if resposta.status_code == 200:
            flash(message="Encomenda cadastrada com sucesso")
            return render_template("ongs.html")
        else:
            flash(message="Erro ao cadastrar")

    return render_template("cadastro_ong.html")


@app.route("/login_da_ong", methods=["POST"])
def login_ong():
    if request.method == 'POST':
        cnpj = request.form.get("cnpj")
        senha = request.form.get("senha")
        resposta = post_login_usuario(cnpj, senha)

        dados_ = resposta.json()
        print(dados_)
        if resposta.status_code == 201:
            flash(message="Encomenda cadastrada com sucesso")
        else:
            flash(message="Erro ao cadastrar")

        return render_template("login_ong.html")


@app.route("/animal_post", methods=["POST"])
def cadastro_animal():
    if request.method == 'POST':
        nome = request.form.get("nome")
        porte = request.form.get("porte")
        sexo = request.form.get("sexo")
        raca = request.form.get("raca")
        adotado = request.form.get("adotado")
        idade = request.form.get("idade")

        resposta = post_animal(nome=nome, porte=porte, sexo=sexo, raca=raca, adotado=adotado, idade=idade)

        dados_ = resposta.json()
        print(dados_)
        if resposta.status_code == 201:
            flash(message="Encomenda cadastrada com sucesso")
        else:
            flash(message="Erro ao cadastrar")

        return render_template("cadastro_animal.html")


        # Passa a lista de animais para o seu template HTML
    return render_template("cadastro_animal.html")


@app.route("/animal_get", methods=["GET"])
def listar_animais():
    animais = get_animais()
    return render_template("adotar.html", animais=animais)


@app.route("/denuncia_post", methods=["GET", "POST"])
def criar_denuncia_anonima():
    if request.method == 'POST':
        descricao = request.form.get("descricao")
        urgencia = request.form.get("urgencia")
        estado = request.form.get("estado")

        resposta = post_denuncia(descricao, urgencia, estado)

        dados_ = resposta.json()
        print(dados_)
        if resposta.status_code == 200:
            flash(message="Encomenda cadastrada com sucesso")
        else:
            flash(message="Erro ao cadastrar")

        denuncia = get_denuncia()
    return render_template("denuncia_anonima.html")


@app.route("/denuncia_get", methods=["GET"])
def listar_denuncia_anonima():
    denuncia = get_denuncia()
    return render_template("ver_denuncias.html", denuncia=denuncia)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
