from api import db
from ..models import assistente_model

casamento_assistente = db.Table('casamento_assistente',
                                db.Column('casamento_id', db.Integer, db.ForeignKey('casamento.id'), primary_key=True, nullable=False),
                                db.Column('assistente.id', db.Integer, db.ForeignKey('assistente.id'), primary_key=True, nullable=False))

class Casamento(db.Model):
    __tablename__ = 'casamento'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    data_casamento = db.Column(db.Date, nullable=False)

    assistentes = db.relationship(assistente_model.Assistente, secondary='casamento_assistente', back_populates='casamentos')

