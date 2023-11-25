from ..models import casamento_model
from api import db
from ..services.assistente_service import assistente_detail

def cadastrar_casamento(casamento):
    casamento_db = casamento_model.Casamento(name=casamento.name, data_casamento=casamento.data_casamento)

    for i in casamento.assistentes:
        assistente = assistente_detail(i)
        casamento_db.assistentes.append(assistente)

    db.session.add(casamento_db)
    db.session.commit()
    return casamento_db

def listar_casamentos():
    casamentos = casamento_model.Casamento.query.all()
    return casamentos

def casamento_detail(id):
    casamento = casamento_model.Casamento.query.filter_by(id=id).first()
    return casamento

def editar_casamento(casamento_bd, casamento_novo):
    casamento_bd.name = casamento_novo.name
    casamento_bd.data_casamento = casamento_novo.data_casamento
    casamento_bd.assistentes = []
    for i in casamento_novo.assistentes:
        assistente = assistente_detail(i)
        casamento_bd.assistentes.append(assistente)
    db.session.commit()

def remover_casamento(casamento):
    db.session.delete(casamento)
    db.session.commit()