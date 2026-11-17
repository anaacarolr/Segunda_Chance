import email
from os.path import exists

from flask import Flask, request, render_template, flash, redirect, url_for
from flask_jwt_extended import JWTManager
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from routes.routes import (post_login_usuario, post_usuario, post_ong, post_animal, post_denuncia, get_denuncia,
                           get_animais, post_verificar_email, get_cnpj, post_verificar_cnpj, post_login_ong)

from flask_login import LoginManager, current_user

app = Flask(__name__)


# Definir a SENHA, em produção colocar em lugar SEGURO
app.config['SECRET_KEY'] = 'Segund@_ch@nc&'

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message = 'Faça login para acessar o sistema'
login_manager.init_app(app)


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
        if not nome:
            flash("Nome obrigatório", 'alert-danger')
            return redirect(url_for("cadastrar_usuario"))
        if not email:
            flash("Email obrigatório", 'alert-danger')
            return redirect(url_for("cadastrar_usuario"))
        if not senha:
            flash("Senha obrigatório", 'alert-danger')
            return redirect(url_for("cadastrar_usuario"))

        #verificar se ja existe usuario com o mesmo email
        email_existe = post_verificar_email(email=email)
        print(email_existe)
        if email_existe["email_existente"]:
            flash("Email existente", 'alert-danger')
            return redirect(url_for("cadastrar_usuario"))
        else:
            flash("Cadstrado com sucesso", 'sucess')

        try:
            new_user = post_usuario(nome=nome, email=email, senha=senha)

            if new_user.status_code == 201:
                flash(message="Usuário cadastrado com sucesso")
                return redirect(url_for("login_usuarios"))
            else:
                flash("Tente Novamente", 'alert-danger')
                return redirect(url_for("cadastrar_usuario"))
        except Exception as e:
            print(e)
            return redirect(url_for("login_usuarios"))
    return render_template("cadastro.html")


@app.route("/login", methods=["GET", "POST"])
def login_usuarios():
    if request.method == 'POST':
        email = request.form.get('form_email')
        senha = request.form.get('form_senha')
        if not email:
            flash("Email obrigatório", 'alert-danger')
            return redirect(url_for("login_usuarios"))
        if not senha:
            flash("Senha obrigatório", 'alert-danger')
            return redirect(url_for("login_usuarios"))

        email_verificado = post_verificar_email(email)
        print('email',email_verificado)
        if email_verificado['email_existente'] == True:  # se encontrou o usuario pelo email
            print(email_verificado)
            login_usuario = post_login_usuario(email=email, senha=senha)
            print('login',login_usuario)
            if login_usuario.status_code == 200:
                return redirect(url_for("listar_animais"))
            else:
                flash("Senha incorreta", "alert")
        else:
            return redirect(url_for('login_usuarios'))
    return render_template('login.html')


@app.route("/post_ong", methods=["GET", "POST"])
def cadastrar_ong():
    if request.method == 'POST':

        cnpj = request.form.get("form-cnpj")
        senha = request.form.get("form-senha")

        if not cnpj:
            flash("CNPJ obrigatório", 'alert-danger')
            return redirect(url_for("cadastrar_ong"))

        if not senha:
            flash("Senha obrigatório", 'alert-danger')
            return redirect(url_for("cadastrar_ong"))

        # chamar a funcao
        cnpj_existe = post_verificar_cnpj(cnpj=cnpj)
        # verificar se ja existe usuario com o mesmo cnpj
        if cnpj_existe["cnpj_existente"]:
            flash("CNPJ existente", 'alert-danger')
            return redirect(url_for("cadastrar_ong"))

        # api de CNPJ
        cnpj_ativo = get_cnpj(cnpj=cnpj)
        print(cnpj_ativo)
        if cnpj_ativo["estabelecimento"]["situacao_cadastral"] != "Ativa":
            flash("CNPJ existente", 'alert-danger')
            return redirect(url_for("cadastrar_ong"))

        nome = cnpj_ativo["razao_social"]
        estado = cnpj_ativo["estabelecimento"]["estado"]["nome"]

        try:
            new_ong = post_ong(nome=nome, cnpj=cnpj, estado=estado, senha=senha)

            if new_ong.status_code == 201:
                flash("ONG cadastrada com sucesso", 'alert-danger')
                return redirect(url_for("login_ong"))
            else:
                flash("Tente Novamente", 'alert-danger')
                return redirect(url_for("cadastrar_ong"))
        except Exception as e:
            print(e)
            return redirect(url_for("login_ong"))
    return render_template("cadastro_ong.html")


@app.route("/login_da_ong", methods=["GET", "POST"])
def login_ong():
    if request.method == 'POST':
        cnpj = request.form.get('form_cnpj')
        senha = request.form.get('form_senha')
        if not cnpj:
            flash("CNPJ obrigatório", 'alert-danger')
            return redirect(url_for("login_ong"))
        if not senha:
            flash("Senha obrigatório", 'alert-danger')
            return redirect(url_for("login_ong"))

        cnpj_verificado = post_verificar_cnpj(cnpj)
        if cnpj_verificado["cnpj_existente"] == True:  # se encontrou o usuario pelo email
            print(cnpj_verificado)
            login_usuario = post_login_ong(cnpj=cnpj, senha=senha)
            print('log',login_usuario)
            if login_usuario['msg'] == "ONG logada com sucesso":
                return redirect(url_for("ongs"))
            else:
                flash("Senha incorreta", "alert")
        else:
            return redirect(url_for('login_ong'))
    return render_template('login_ong.html')


@app.route("/animal_post", methods=["GET", "POST"])
def cadastro_animal():
    if request.method == 'POST':
        print("qwe")
        nome = request.form.get("form-nome")
        porte = request.form.get("form-porte")
        print(porte)
        sexo = request.form.get("sexo")
        raca = request.form.get("form-raca")
        idade = request.form.get("form-idade")
        categoria = request.form.get("form-categoria")
        id_user = request.form.get("form-id_user")

        if not nome:
            print("nome")
            flash("Nome obrigatório", 'alert-danger')
            return redirect(url_for("cadastro_animal"))
        if not porte:
            print("porte")
            flash("Porte obrigatório", 'alert-danger')
            return redirect(url_for("cadastro_animal"))
        if not sexo:
            print("sexo")
            flash("Sexo obrigatório", 'alert-danger')
            return redirect(url_for("cadastro_animal"))
        if not raca:
            print("raca")
            flash("Raça obrigatório", 'alert-danger')
            return redirect(url_for("cadastro_animal"))
        if not idade:
            print('idade')
            flash("Idade obrigatório", 'alert-danger')
            return redirect(url_for("cadastro_animal"))
        if not categoria:
            print('categoria')
            flash("Categoria obrigatória", 'alert-danger')
            return redirect(url_for("cadastro_animal"))

        try:
            new_animal = post_animal(nome=nome, id_user=id_user, categoria=categoria, porte=porte, sexo=sexo, raca=raca, idade=idade)

            if new_animal.status_code == 201:
                flash("Animal cadastrado com sucesso", 'alert-danger')
                return redirect(url_for("ongs"))
            else:
                flash("Tente Novamente", 'alert-danger')
                print("hhk",new_animal.status_code)
                return redirect(url_for("cadastro_animal"))
        except Exception as e:
            print(e)
            return redirect(url_for("ongs"))
    return render_template("cadastro_animal.html")


@app.route("/animal_get", methods=["GET"])
def listar_animais():
    animais = get_animais()

    return render_template("adotar.html", animais=animais)


@app.route("/denuncia_post", methods=["GET", "POST"])
def criar_denuncia_anonima():
    if request.method == 'POST':
        descricao = request.form.get("form-descricao")
        urgencia = request.form.get("form-urgencia")
        estado = request.form.get("form-estado")

        if not descricao:
            flash("Descrição obrigatório", 'alert-danger')
            return redirect(url_for("criar_denuncia_anonima"))
        print("DESCRICAO")
        if not estado:
            flash("estado obrigatório", 'alert-danger')
            return redirect(url_for("criar_denuncia_anonima"))
        print("ESTADO")

        # fazer um if na urgencia para quando vier none colocar false e se nao colocar true
        if urgencia is None:
            urgencia = "Não"
        else:
            urgencia = "Sim"

        try:
            new_denuncia = post_denuncia(descricao=descricao, urgencia=urgencia, estado=estado)

            if new_denuncia.status_code == 201:
                flash("Denuncia cadastrada com sucesso", 'alert-danger')
                return redirect(url_for("listar_animais"))
            else:
                flash("Tente Novamente", 'alert-danger')
                return redirect(url_for("criar_denuncia_anonima"))
        except Exception as e:
            print(e)
            return redirect(url_for("listar_animais"))
    return render_template("denuncia_anonima.html")

    '''
    if request.method == 'POST':
        descricao = request.form.get("descricao")
        urgencia = request.form.get("urgencia")
        estado = request.form.get("estado")

        resposta = post_denuncia(descricao, urgencia, estado)

        dados_ = resposta.json()
        print(dados_)
        if resposta.status_code == 200:
            flash(message="Denuncia feita com sucesso")
        else:
            flash(message="Erro ao cadastrar")

        denuncia = get_denuncia()
    return render_template("denuncia_anonima.html")
    '''

'''
@app.route("/denuncia_get", methods=["GET"])
def listar_denuncia_anonima():
    denuncia = get_denuncia('denuncia')
    return render_template("ver_denuncias.html", denuncia=denuncia)
'''


'''
@app.route("/animais_get", methods=["GET"]))
def listar_animais():
    animais = get_animais()
    return render_template("ver_animais.html", animais=animais)
'''

@app.route("/denuncia_get", methods=["GET"])
def listar_denuncia_anonima():
    denuncia = get_denuncia()
    print(denuncia)
    return render_template("ver_denuncias.html", denuncia=denuncia)

'''
@app.route("/")
def base():
    list_p = get_products()['products']
    return render_template('base.html', list_p=list_p)
'''


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
