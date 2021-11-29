from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.contato import Contato
from utils.db import db


contatos = Blueprint('contatos', __name__)


@contatos.route('/')
def index():
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

    flash("Contato adicionado!")

    return redirect(url_for('contatos.index')) 


@contatos.route('/atualiza/<id>', methods = ['POST', 'GET'])
def upd_contato(id):
    contato = Contato.query.get(id)
    
    if request.method == 'POST':
        contato = Contato.query.get(id)
        contato.nome = request.form["nome"]
        contato.email = request.form["email"]
        contato.telefone = request.form["telefone"]

        db.session.commit()

        flash("Contato atualizado!")

        return redirect(url_for("contatos.index"))

    return render_template('update.html', contato=contato)


@contatos.route('/remove/<id>')
def del_contato(id):
    contato = Contato.query.get(id)
    db.session.delete(contato)
    db.session.commit()

    flash("Contato removido!")

    return redirect(url_for('contatos.index'))   


@contatos.route('/sobre')
def sobre():
    return render_template('sobre.html')