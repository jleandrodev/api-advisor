from enum import Enum
from api import db
from ..models import convidado_model

class FaixaEtaria(Enum):
    ZERO_CINCO_ANOS = "0-5 anos"
    SEIS_DEZ_ANOS = "6-10 anos"
    ADULTO = "Adulto"
class Acompanhante(db.Model):
    __tablename__ = 'acompanhante'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    idade = db.Column(db.String(12), nullable=False)

    convidado_id = db.Column(db.Integer, db.ForeignKey("convidado.id"))
    convidado = db.relationship(convidado_model.Convidado, back_populates='acompanhantes')