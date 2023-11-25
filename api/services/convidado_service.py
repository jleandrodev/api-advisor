from ..models import convidado_model
from api import db

def cadastrar_convidado(convidado):
    convidado_db = convidado_model.Convidado(nome=convidado.nome, telefone=convidado.telefone, casamento=convidado.casamento)

    db.session.add(convidado_db)
    db.session.commit()
    return convidado_db

def listar_convidados():
    convidados = convidado_model.Convidado.query.all()
    return convidados

def convidado_detail(id):
    convidado = convidado_model.Convidado.query.filter_by(id=id).first()
    return convidado

def editar_convidado(convidado_bd, convidado_novo):
    convidado_bd.nome = convidado_novo.nome
    convidado_bd.telefone = convidado_novo.telefone
    db.session.commit()

def remover_convidado(convidado):
    db.session.delete(convidado)
    db.session.commit()