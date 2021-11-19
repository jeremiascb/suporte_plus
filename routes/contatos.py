from flask import Blueprint, render_template, request, redirect
from werkzeug.utils import redirect
from models.contato import Contato
from utils.db import db

contatos = Blueprint('contatos', __name__)

@contatos.route('/')
def home():
    contatos = Contato.query.all()
    return render_template('index.html', contatos=contatos)

@contatos.route('/novo', methods=['POST'])
def add_contato():
    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']

    novo_contato = Contato(nome, email, telefone)

    db.session.add(novo_contato)
    db.session.commit()

    return redirect('/')

@contatos.route('/atualiza')
def upd_contato():
    return "Atulizando o contato"

@contatos.route('/remove')
def del_contato():
    return "Removendo o contato"   

@contatos.route('/sobre')
def sobre():
    return render_template('sobre.html')