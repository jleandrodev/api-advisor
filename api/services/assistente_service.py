from ..models import assistente_model
from api import db

def cadastrar_assistente(assistente):
    casameno_db = assistente_model.Assistente(nome=assistente.nome, telefone=assistente.telefone)

    db.session.add(casameno_db)
    db.session.commit()
    return casameno_db

def listar_assistentes():
    assistentes = assistente_model.Assistente.query.all()
    return assistentes

def assistente_detail(id):
    assistente = assistente_model.Assistente.query.filter_by(id=id).first()
    return assistente

def editar_assistente(assistente_bd, assistente_novo):
    assistente_bd.nome = assistente_novo.nome
    assistente_bd.telefone = assistente_novo.telefone
    db.session.commit()

def remover_assistente(assistente):
    db.session.delete(assistente)
    db.session.commit()