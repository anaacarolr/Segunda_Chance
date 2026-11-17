from flask import Flask, jsonify
import datetime
from dateutil.relativedelta import relativedelta

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Validade de Produtos</h1>"

@app.route("/data_vencimento/<data_entrada>")
def verificar_validade(data_entrada):
    try:
        data_venc = datetime.datetime.strptime(data_entrada, '%d-%m-%Y').date()
        hoje = datetime.date.today()

        if data_venc < hoje:
            situacao = "PRODUTO VENCIDO"
        elif data_venc == hoje:
            situacao = "VENCE HOJE"
        else:
            situacao = "DENTRO DA VALIDADE"

        diff = relativedelta(data_venc, hoje)

        dados = {
            "situacao": situacao,
            "data_produto": data_venc.strftime('%d/%m/%Y'),
            "data_hoje": hoje.strftime('%d/%m/%Y'),
            "tempo_restante": {
                "anos": abs(diff.years),
                "meses": abs(diff.months),
                "dias": abs(diff.days),
                "total_dias_corridos": abs((data_venc - hoje).days)
            }
        }
        return jsonify(dados), 200

    except ValueError:
        return jsonify({"erro": "Formato inválido! Use DD-MM-YYYY"}), 400

if __name__ == "__main__":
    app.run(debug=True, port=5003)
