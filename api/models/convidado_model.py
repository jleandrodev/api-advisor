from api import db
from ..models import casamento_model

class Convidado(db.Model):
    __tablename__ = 'convidado'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    telefone = db.Column(db.String(11), nullable=False)

    casamento_id = db.Column(db.String, db.ForeignKey("casamento.id"))
    casamento = db.relationship(casamento_model.Casamento, backref=db.backref('convidados', lazy='dynamic'))

    acompanhantes = db.relationship('Acompanhante', back_populates='convidado')
