from flask_restful import Resource
from api import api
from flask import request, make_response, jsonify
from flask_jwt_extended import jwt_required
from ..schemas import assistente_schema
from ..entidades import assistente
from ..services import assistente_service

class Assistente(Resource):
    @jwt_required()
    def get(self):
        assistentes = assistente_service.listar_assistentes()
        a_s = assistente_schema.AssistenteSchema(many=True)
        return make_response(a_s.jsonify(assistentes), 200)
    
    @jwt_required()
    def post(self):
        a_s = assistente_schema.AssistenteSchema()
        validate = a_s.validate(request.json)

        if validate:
            make_response(jsonify(validate), 400)
        else:
            nome = request.json['nome']
            telefone = request.json['telefone']

            novo_assistente = assistente.Assistente(nome=nome, telefone=telefone)

            result = assistente_service.cadastrar_assistente(novo_assistente)

            return make_response(a_s.jsonify(result), 201)
        
class AssistenteDetails(Resource):
    @jwt_required()
    def get(self, id):
        assistente = assistente_service.assistente_detail(id)
        if assistente is None:
            return make_response("Assistente não encontrado!", 404)
        
        a_s = assistente_schema.AssistenteSchema()
        return make_response(a_s.jsonify(assistente), 200)

    @jwt_required()
    def put(self, id):
        assistente_bd = assistente_service.assistente_detail(id)
        if assistente_bd is None:
            return make_response("Assistente não encontrado!", 404)
        
        a_s = assistente_schema.AssistenteSchema()
        validate = a_s.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json['nome']
            telefone = request.json['telefone']
            assistente_novo = assistente.Assistente(nome=nome, telefone=telefone)

            assistente_service.editar_assistente(assistente_bd, assistente_novo)
            assistente_atualizado = assistente_service.assistente_detail(id)
            return make_response(a_s.jsonify(assistente_atualizado), 200)

    @jwt_required()
    def delete(self, id):
        assistente = assistente_service.assistente_detail(id)
        if assistente is None:
            return make_response("Assistente não encontrado!", 404)
        
        assistente_service.remover_assistente(assistente)

        return make_response("", 204)

    
api.add_resource(Assistente, '/assistentes')
api.add_resource(AssistenteDetails, '/assistentes/<int:id>')