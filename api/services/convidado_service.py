from ..models import convidado_model, acompanhante_model
from ..entidades.convidado import Convidado
from api import db

def cadastrar_convidado(convidado):
    novo_convidado = Convidado(nome=convidado.nome, telefone=convidado.telefone, casamento=convidado.casamento, acompanhantes=convidado.acompanhantes)
    convidado_db = convidado_model.Convidado(nome=novo_convidado.nome, telefone=novo_convidado.telefone, casamento_id=novo_convidado.casamento)
    if not isinstance(convidado_db, convidado_model.Convidado):
        raise ValueError("O objeto `convidado` não é uma instância válida de Convidado.")

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