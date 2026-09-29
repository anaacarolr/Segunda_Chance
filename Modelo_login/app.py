from flask import Flask, render_template, url_for, flash, request, redirect
from sqlalchemy.exc import SQLAlchemyError

from database import db_session, Usuario
from sqlalchemy import select, and_, func
from flask_login import LoginManager, login_required, login_user, logout_user, current_user

app = Flask(__name__)
# mover para .env
app.config['SECRET_KEY'] = '1234'

login_manager = LoginManager(app)
login_manager.login_view = 'login'


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@login_manager.user_loader
def load_user(user_id):
    user = select(Usuario).where(Usuario.id == int(user_id))
    resultado = db_session.execute(user).scalar_one_or_none()
    return resultado


@app.route('/')
@login_required
def index():
    # haverá processos aqui
    return render_template('index.html')


@app.route('/teste', methods=['GET'])
@login_required
def teste_():
    return render_template('teste.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('form-email')
        senha = request.form.get('form-senha')

        if email and senha:
            verificar_email = select(Usuario).where(Usuario.email == email)
            resultado_email = db_session.execute(verificar_email).scalar_one_or_none()
            if resultado_email:
                # se encontrado na base de dados
                if resultado_email.check_password(senha):
                    # login correto
                    login_user(resultado_email)
                    flash(f'Logado com sucesso', 'success')
                    return redirect(url_for('index'))
                else:
                    # login incorreto
                    flash('Senha incorreta', 'danger')
                    return render_template('login.html')
            else:
                # se não encontrado
                flash(f'Email nao encontrado', 'danger')
                return render_template('login.html')
        else:
            flash('Preencha todos os campos', 'danger')
            return render_template('login.html')
    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    logout_user()
    flash('Logout com sucesso', 'success')
    return redirect(url_for('login'))


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro_usuario():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        if not nome or not email or not senha:
            flash('Por favor preencher os campos', 'danger')
            return render_template('cadastro.html')
        verificar_email = select(Usuario).where(Usuario.email == email)
        exists_email = db_session.execute(verificar_email).scalar_one_or_none()
        if exists_email:
            flash(f'Email {email} ja esta cadastrado', 'danger')
            return render_template('cadastro.html')
        try:
            novo_usuario = Usuario(nome=nome, email=email)
            novo_usuario.set_password(senha)
            db_session.add(novo_usuario)
            db_session.commit()
            flash(f'Usuario {nome} cadastrado com sucesso', 'success')
            return redirect(url_for('login'))
        except SQLAlchemyError as e:
            flash(f'Erro na base de dados ao cadastrar usuario: {e}', 'danger')
            print(f'Erro na base de dados:{e}')
            return redirect(url_for('login'))
        except Exception as e:
            flash(f'Erro ao cadastrar usuario: {e}', 'danger')
            print(f'Erro ao cadastrar:{e}')
            return redirect(url_for('cadastro_usuario'))
    return render_template('cadastro.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
