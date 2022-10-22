from app import app
from flask import render_template

@app.route('/')

@app.route('/index')
def index():
    nomedealguem = 'Carlinhos'
    dados = {"profissao":"Autônomo","canal":"Não tenho"}
    return render_template('index.html',nome = nomedealguem, dados=dados)

@app.route('/contato')
def contato():
    return render_template('contato.html')