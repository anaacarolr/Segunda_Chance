from flask import Flask, render_template, url_for, flash, request, redirect
from routes.rotas import get_products
from sqlalchemy.exc import SQLAlchemyError

from sqlalchemy import select, and_, func

app = Flask(__name__)
app.config['SECRET_KEY'] = 'amora123'

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/produtos')
def produtos():
    list_p = get_products()['products']
    return render_template('produtos.html', list_p=list_p)



#TODO Final do código

if __name__ == '__main__':
    app.run(debug=True, port=5000)