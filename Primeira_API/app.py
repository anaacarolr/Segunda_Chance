from flask import Flask

app = Flask(__name__)
@app.route('/')
def home():
    return '<h1>Hello World!</h1>'

@app.route('/<nome>')
def saudacao(nome):
    return f'ola {nome}'

@app.route('/divisao/<n1>/<n2>')
def divisao(n1, n2):
    try:
        n1 = int(n1)
        n2 = int(n2)
        return f'{n1} / {n2} = {n1 / n2}'
    except ValueError:
        return f'Apenas numero'
    except ZeroDivisionError:
        return f'...'

@app.route('/multiplicacao/<n3>/<n4>')
def multiplicacao(n3, n4):
    try:
        n3 = int(n3)
        n4 = int(n4)
        return f'{n3} * {n4} = {n3 * n4}'
    except ValueError:
        return f'Apenas numero'
    except ZeroDivisionError:
        return f'...'


@app.route('/subtracao/<n1>/<n2>')
def subtracao(n5, n6):
    try:
        n5 = int(n5)
        n6 = int(n6)
        return f'{n5} - {n6} = {n5 - n6}'
    except ValueError:
        return f'Apenas numero'
    except ZeroDivisionError:
        return f'...'

@app.route('/soma/<n1>/<n2>')
def soma(n7, n8):
    try:
        n7 = int(n7)
        n8 = int(n8)
        return f'{n7} + {n8} = {n7 + n8}'
    except ValueError:
        return f'Apenas numero'
    except ZeroDivisionError:
        return f'...'


@app.route('/verifica/<numero>')
def verifica(numero):
    try:
        n = int(numero)
        tipo = 'par' if n % 2 == 0 else 'impar'
        return f'O número {n} é {tipo}'
    except ValueError:
        return 'Digite um número inteiro válido'


if __name__ == '__main__':
    app.run(debug=True, port=5004)