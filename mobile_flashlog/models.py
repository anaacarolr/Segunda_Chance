import requests

base_url = "http://10.135.232.12:5000"

def get_encomenda_por_codigo(codigo):
    url = f"{base_url}/api/encomendas"
    try:
        response = requests.get(url, params={"codigo": codigo})
        if response.status_code == 200:
            dados = response.json()
            return dados["pacotes"][0] if dados.get("pacotes") else None
        return None
    except Exception:
        return None

def get_movimentacoes_por_pacote(pacote_id):
    url = f"{base_url}/api/movimentacoes"
    try:
        response = requests.get(url, params={"pacote_id": pacote_id})
        if response.status_code == 200:
            return response.json().get("movimentacoes", [])
        return []
    except Exception:
        return []
