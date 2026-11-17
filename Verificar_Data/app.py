from flask import Flask, jsonify
import datetime
#from datetime import datetime

app = Flask(__name__)

tempo = datetime.datetime.now()

@app.route("/")
def home():
    return "<h1>Verificar data</h1>"

@app.route("/data/<data_entrada>")
def maior_menor(n1, n2):
    n1 = int(n1)
    n2 = int(n2)
    if n1 > n2:
        return f'N1 {n1} e maior que N2 {n2}'
        """dados =
            {
            'nome_n1: n1,
            'nome_n2: n2,
        }
        return jsonfy(dados)"""
    else:
        return f'N1 {n1} e maior que N2 {n2}'

@app.route("/verificar-data/<data_entrada>")
def verificar_data(data_entrada):
    data_convertida = (datetime.datetime.strptime(data_entrada, '%d-%m-%Y')).date()
    agora_today = (datetime.datetime.today()).date()
    if data_convertida > agora_today:
        var_situacao = f'Futuro {data_convertida}'
    elif data_convertida <= agora_today:
        var_situacao = f'Presente {data_convertida}'
    else:
        var_situacao = f'Passado {data_convertida}'

    tentar_diferenca_dia = (data_convertida - agora_today).days
    tentar_diferenca_ano = (data_convertida.year - agora_today.year)
    tentar_diferenca_mes = ((data_convertida.month - agora_today.month)+(12 * tentar_diferenca_ano))
    print(f'teste:{tentar_diferenca_dia}')
    print(f'teste_mes:{tentar_diferenca_mes}')
    print(f'teste_ano:{tentar_diferenca_ano}')

    dados = {
        "situacao": var_situacao,
        "dias_diferenca": abs(int(tentar_diferenca_dia)),
        "difereca_meses": abs(tentar_diferenca_mes),
        "diferenca_ano": abs(tentar_diferenca_ano)
    }

    return jsonify(dados),200

print(f'{tempo}')
# tratar datas
print(f'Ano: {tempo.year}-Mes:{tempo.month}-Dia:{tempo.day}')

# tempo.strftime para configurar modo de exibicao
print(tempo.strftime('%A %d,%B %Y %I:%M %p'))

# tratar horas
print(f'Hora: {tempo.hour} |Minuto: {tempo.minute} |Segundo: {tempo.second}')

print(f'Dia: {tempo.day}')
print(f'Mês: {tempo.month}')
print(f'Ano: {tempo.year}')


if __name__ == "__main__":
    app.run(debug=True, port=5003)