from ..models import acompanhante_model
from api import db

def cadastrar_acompanhante(acompanhante):
    acompanhante_db = acompanhante_model.Acompanhante(nome=acompanhante.nome, idade=acompanhante.idade, convidado_id=acompanhante.convidado)

    db.session.add(acompanhante_db)
    db.session.commit()
    return acompanhante_db

def listar_acompanhantes():
    acompanhantes = acompanhante_model.Acompanhante.query.all()
    return acompanhantes

def acompanhante_detail(id):
    acompanhante = acompanhante_model.Acompanhante.query.filter_by(id=id).first()
    return acompanhante

def editar_acompanhante(acompanhante_bd, acompanhante_novo):
    acompanhante_bd.nome = acompanhante_novo.nome
    acompanhante_bd.idade = acompanhante_novo.idade
    db.session.commit()

def remover_acompanhante(acompanhante):
    db.session.delete(acompanhante)
    db.session.commit()