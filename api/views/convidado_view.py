from flask_restful import Resource
from flask_jwt_extended import jwt_required
from api import api
from flask import request, make_response, jsonify
from ..schemas import convidado_schema
from ..entidades import convidado
from ..services import convidado_service, casamento_service

class Convidado(Resource):
    @jwt_required()
    def get(self):
        convidados = convidado_service.listar_convidados()
        cs = convidado_schema.ConvidadoSchema(many=True)
        return make_response(cs.jsonify(convidados), 200)
    
    @jwt_required()
    def post(self):
        cs = convidado_schema.ConvidadoSchema()
        validate = cs.validate(request.json)

        if validate:
            make_response(jsonify(validate), 400)
        else:
            nome = request.json['nome']
            telefone = request.json['telefone']
            casamento = request.json['casamento']

            casamento_convidado = casamento_service.casamento_detail(casamento)
            if casamento_convidado is None:
                return make_response("Casamento não encontrado", 404)

            novo_convidado = convidado.Convidado(nome=nome, telefone=telefone, casamento=casamento_convidado)

            result = convidado_service.cadastrar_convidado(novo_convidado)

            return make_response(cs.jsonify(result), 201)
        
class ConvidadoDetails(Resource):
    @jwt_required()
    def get(self, id):
        convidado = convidado_service.convidado_detail(id)
        if convidado is None:
            return make_response("Convidado não encontrado!", 404)
        
        cs = convidado_schema.ConvidadoSchema()
        return make_response(cs.jsonify(convidado), 200)

    @jwt_required()
    def put(self, id):
        convidado_bd = convidado_service.convidado_detail(id)
        if convidado_bd is None:
            return make_response("Convidado não encontrado!", 404)
        
        cs = convidado_schema.ConvidadoSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json['nome']
            telefone = request.json['telefone']
            casamento = request.json['casamento']
            convidado_novo = convidado.Convidado(nome=nome, telefone=telefone, casamento=casamento)

            convidado_service.editar_convidado(convidado_bd, convidado_novo)
            convidado_atualizado = convidado_service.convidado_detail(id)
            return make_response(cs.jsonify(convidado_atualizado), 200)

    @jwt_required()
    def delete(self, id):
        convidado = convidado_service.convidado_detail(id)
        if convidado is None:
            return make_response("Convidado não encontrado!", 404)
        
        convidado_service.remover_convidado(convidado)

        return make_response("", 204)

    
api.add_resource(Convidado, '/convidados')
api.add_resource(ConvidadoDetails, '/convidados/<int:id>')