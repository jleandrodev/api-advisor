from flask_jwt_extended import jwt_required
from flask_restful import Resource
from api import api
from flask import request, make_response, jsonify
from ..schemas import casamento_schema
from ..entidades import casamento
from ..services import casamento_service

class Casamento(Resource):
    @jwt_required()
    def get(self):
        casamentos = casamento_service.listar_casamentos()
        cs = casamento_schema.CasamentoSchema(many=True)
        return make_response(cs.jsonify(casamentos), 200)
    @jwt_required()
    def post(self):
        cs = casamento_schema.CasamentoSchema()
        validate = cs.validate(request.json)

        if validate:
            return make_response(jsonify(validate), 400)
        else:
            name = request.json['name']
            data_casamento = request.json['data_casamento']
            assistentes = request.json['assistentes']

            novo_casamento = casamento.Casamento(name=name, data_casamento=data_casamento, assistentes=assistentes)

            result = casamento_service.cadastrar_casamento(novo_casamento)

            return make_response(cs.jsonify(result), 201)

        
class CasamentoDetails(Resource):
    @jwt_required()
    def get(self, id):
        casamento = casamento_service.casamento_detail(id)
        if casamento is None:
            return make_response("Casamento não encontrado!", 404)
        
        cs = casamento_schema.CasamentoSchema()
        return make_response(cs.jsonify(casamento), 200)
    
    @jwt_required()
    def put(self, id):
        casamento_bd = casamento_service.casamento_detail(id)
        if casamento_bd is None:
            return make_response("Casamento não encontrado!", 404)
        
        cs = casamento_schema.CasamentoSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            name = request.json['name']
            data_casamento = request.json['data_casamento']
            assistentes = request.json['assistentes']
            casamento_novo = casamento.Casamento(name=name, data_casamento=data_casamento, assistentes=assistentes)

            casamento_service.editar_casamento(casamento_bd, casamento_novo)
            casamento_atualizado = casamento_service.casamento_detail(id)
            return make_response(cs.jsonify(casamento_atualizado), 200)
        
    @jwt_required()
    def delete(self, id):
        casamento = casamento_service.casamento_detail(id)
        if casamento is None:
            return make_response("Casamento não encontrado!", 404)
        
        casamento_service.remover_casamento(casamento)

        return make_response("", 204)

    
api.add_resource(Casamento, '/casamentos')
api.add_resource(CasamentoDetails, '/casamentos/<int:id>')








