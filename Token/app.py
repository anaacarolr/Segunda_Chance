import cpf
from flask import Flask, jsonify,request
from sqlalchemy import select
from models import UsuarioExemplo, NotasExemplo, SessionLocalExemplo, Funcionario
#gerar token
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager
#gerar os papes
from functools import wraps


app = Flask(__name__)
app.config['SECRET_KEY'] = 'amora123'
jwt = JWTManager(app)

def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        current_user = get_jwt_identity()
        print(f"User:{current_user}")

        db = SessionLocalExemplo()
        try:
            sql = select(UsuarioExemplo).where(UsuarioExemplo.email == current_user)
            usuario_existente = db.execute(sql).scalar()
            print(f"Usuario existente: {usuario_existente}")
            if usuario_existente and usuario_existente.papel == "admin":
                return fn(*args, **kwargs)
            dados = {
                "msg":"Acesso negado: Requer privilégio de administrador"
            }
            return jsonify()
        finally:
            db.close()

@app.route('/login', methods=['POST'])
def login():
    try:
        dados_entrada = request.get_json()
        email = dados_entrada['email']
        senha = dados_entrada['senha']

        db = SessionLocalExemplo()
        sql = select(UsuarioExemplo).where(UsuarioExemplo.email == email)
        usuario_existente = db.execute(sql).scalar()

        if usuario_existente and usuario_existente.check_password(senha):
            access_token = create_access_token(identity=usuario_existente.email)
            dados= {
                "access_token": access_token,
                "papel": usuario_existente.papel,
            }
            return jsonify(dados), 200
        dados = {
            "msg":"Credenciais"
        }
        return jsonify(dados), 401
    except Exception as e:
        return jsonify({"msg": str(e)}), 400
    finally:
        db.close()

@app.route('/cadastro', methods=['POST'])
def cadastro():
    dados = request.get_json()
    nome = dados['nome']
    email = dados['email']

    if not nome or not email:
        return jsonify({"msg": "Nome de usuário e senha são obrigatórios"}), 400

    banco = SessionLocalExemplo()
    try:
        # Verificar se o usuário já existe
        user_check = select(UsuarioExemplo).where(UsuarioExemplo.nome == nome)
        usuario_existente = banco.execute(user_check).scalar()

        if usuario_existente:
            return jsonify({"msg": "Usuário já existe"}), 400

        novo_usuario = UsuarioExemplo(nome=nome, email=email)
        banco.add(novo_usuario)
        banco.commit()

        user_id = novo_usuario.id
        return jsonify({"msg": "Usuário criado com sucesso", "user_id": user_id}), 201
    except Exception as e:
        banco.rollback()
        return jsonify({"msg": f"Erro ao registrar usuário: {str(e)}"}), 500
    finally:
        banco.close()

@app.route('/notas_exemplo', methods=['POST'])
def criar_nota_exemplo():
    data = request.get_json()
    conteudo = data.get('conteudo')

    if not conteudo:
        return jsonify({"msg": "Conteúdo da nota é obrigatório"}), 400

    db = SessionLocalExemplo()
    try:
        nova_nota = NotasExemplo(conteudo=conteudo)
        # Se quisesse associar ao usuário: nova_nota.user_id = current_user_id
        db.add(nova_nota)
        db.commit()
        nota_id = nova_nota.id
        return jsonify({"msg": "Nota criada", "nota_id": nota_id}), 201
    except Exception as e:
        db.rollback()
        return jsonify({"msg": f"Erro ao criar nota: {str(e)}"}), 500
    finally:
        db.close()

@app.route('/funcionarios')
def listar_funcionarios():
    db = SessionLocalExemplo()
    funcionarios_sql = select(Funcionario)
    funcionarios_result = db.execute(funcionarios_sql).scalars().all()

@app.route('/funcionarios_cpf')
def buscar_funcionario_cpf():

   dados = request.get_json()
    user_cpf = select(Funcionario).where(Funcionario.cpf == cpf)
    user_cpf = db_session.execute(user_cpf).scalars().one_or_none()

@app.route('/notas_exemplo', methods=['GET'])
def listar_notas_exemplo():
    db = SessionLocalExemplo()
    try:
        stmt = select(NotasExemplo)
        notas_result = db.execute(stmt).scalars().all() # .scalars().all() para obter uma lista de objetos
        notas_list = [{"id": nota.id, "conteudo": nota.conteudo} for nota in notas_result]
        return jsonify(notas_list)
    finally:
        db.close()

if __name__ == '__main__':
    app.run(debug=True, port=5001, host='0.0.0.0') # Rodar em uma porta diferente da API principal