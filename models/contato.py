from utils.db import db

class Contato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40))
    email = db.Column(db.String(40))
    telefone = db.Column(db.String(20))

    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone