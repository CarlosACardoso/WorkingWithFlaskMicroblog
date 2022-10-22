from app import app
from flask import render_template
from flask import request
#from pymongo import MongoClient

@app.route('/')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')
    dados = {"usuário": usuario, "senha":senha}
  #  client = MongoClient("mongodb+srv://adminuser:adminuser@mygame.t19zp9a.mongodb.net/?retryWrites=true&w=majority")
  #  colocardados = client.get_database("clientslandpage")
  #  dicionario = colocardados.clients_landpage
  #  dicionario.insert_one(dados)

    return f"Seu cadastro foi realizado com sucesso! {dados}"