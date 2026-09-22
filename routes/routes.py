import requests

url = "http://10.135.232.27:5001"

def post_animal(nome, id_user,id_categoria, porte, sexo, raca, adotado, idade):
    url_ = f"{url}/animal_post"
    dados_animal = {
        "nome": nome,
        "id_user": id_user,
        "id_categoria": id_categoria,
        "porte": porte,
        "sexo": sexo,
        "raca": raca,
        "adotado": adotado,
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
    return dados.json()

def post_categoria(nome):
    url_ = f"{url}/categoria_post"
    dados_categoria = {
        "nome": nome,
    }
    dados = requests.post(url_, json=dados_categoria)
    return dados.json()

def post_usuario(nome, senha, email):
    url_ = f"{url}/post_usuario"
    dados_usuario = {
        "nome": nome,
        "email": email,
        "senha": senha
    }
    dados = requests.post(url_, json=dados_usuario)
    return dados.json()

def post_login_usuario(email, senha):
    url_ = f"{url}/login_do_usuario"
    dados_usuario = {
        "email": email,
        "senha": senha
    }
    dados = requests.post(url_, json=dados_usuario)
    return dados.json()

def post_ong(nome, cnpj, estado, senha):
    url_ = f"{url}/cadastrar_ong"
    dados_usuario = {
        "nome": nome,
        "cnpj": cnpj,
        "estado": estado,
        "senha": senha
    }
    dados = requests.post(url_, json=dados_usuario)
    return dados.json()

def post_login_ong(cnpj, senha):
    url_ = f"{url}/login_da_ong"
    dados_usuario = {
        "cnpj": cnpj,
        "senha": senha
    }
    dados = requests.post(url_, json=dados_usuario)
    return dados.json()



def get_animais():
    url_ = f"{url}/animal_get"

    dados = requests.get(url_)
    return dados.json()

def get_denuncia():
    url_ = f"{url}/denuncia_get"

    dados = requests.get(url_)
    return dados.json()

def get_categoria():
    url_ = f"{url}/categoria_get"

    dados = requests.get(url_)
    return dados.json()