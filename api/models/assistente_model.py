from api import db

class Assistente(db.Model):
    __tablename__ = 'assistente'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    telefone = db.Column(db.String(11), nullable=False)

    casamentos = db.relationship("Casamento", secondary='casamento_assistente', back_populates='assistentes')

