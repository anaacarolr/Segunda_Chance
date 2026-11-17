import requests

url = "http://10.135.232.25:5002"

url_cnpj = "https://publica.cnpj.ws"

def post_animal(nome, id_user,categoria, porte, sexo, raca, idade):
    url_ = f"{url}/animal_post"
    dados_animal = {
        "nome": nome,
        "id_user": id_user,
        "categoria": categoria,
        "porte": porte,
        "sexo": sexo,
        "raca": raca,

        "idade": idade
    }

    dados = requests.post(url_, json=dados_animal)
    return dados.json()

def post_denuncia(descricao, urgencia, estado):
    url_ = f"{url}/denuncia_post"
    dados_denuncia = {
        "descricao": descricao,
        "urgencia": urgencia,
        "estado": estado
    }

    dados = requests.post(url_, json=dados_denuncia)
    return dados

def post_usuario(nome, senha, email):
    url_ = f"{url}/post_usuario"
    dados_usuario = {
        "nome": nome,
        "email": email,
        "senha": senha
    }
    dados = requests.post(url_, json=dados_usuario)
    return dados

def post_login_usuario(email, senha):
    url_ = f"{url}/login_do_usuario"
    dados_usuario = {
        "email": email,
        "senha": senha
    }
    dados = requests.post(url_, json=dados_usuario)
    return dados

def post_ong(nome, cnpj, estado, senha):
    url_ = f"{url}/post_ong"
    dados_usuario = {
        "nome": nome,
        "cnpj": cnpj,
        "estado": estado,
        "senha": senha
    }
    dados = requests.post(url_, json=dados_usuario)
    return dados

def post_login_ong(cnpj, senha):
    url_ = f"{url}/login_da_ong"
    dados_usuario = {
        "cnpj": cnpj,
        "senha": senha
    }
    dados = requests.post(url_, json=dados_usuario)
    return dados.json()

def post_verificar_email(email):
    url_ = f"{url}/verificar_email"
    dados = {
        "email": email
    }
    dados = requests.post(url_, json=dados)
    return dados.json()

def post_verificar_cnpj(cnpj):
    url_ = f"{url}/verificar_cnpj"
    dados = {
        "cnpj": cnpj
    }
    dados = requests.post(url_, json=dados)
    return dados.json()


def get_animais():
    url_ = f"{url}/animal_get"

    dados = requests.get(url_)
    return dados.json()

def get_denuncia():
    url_ = f"{url}/denuncia_get"

    dados = requests.get(url_)
    return dados.json()

def get_cnpj(cnpj):
    # 1 - Definir o endpoint que vai ser consumido
    url_ = f"{url_cnpj}/cnpj/{cnpj}"

    # 2 - Fazer a requisição (pedindo os dados)
    dados = requests.get(url_)

    # 3 - Retornar os dados
    return dados.json()

