from flask_restful import Resource
from flask_jwt_extended import jwt_required
from api import api
from flask import request, make_response, jsonify
from ..schemas import acompanhante_schema
from ..entidades import acompanhante
from ..services import acompanhante_service, convidado_service

class Acompanhante(Resource):
    @jwt_required()
    def get(self):
        acompanhantes = acompanhante_service.listar_acompanhantes()
        acs = acompanhante_schema.AcompanhanteSchema(many=True)
        return make_response(acs.jsonify(acompanhantes), 200)
    
    @jwt_required()
    def post(self):
        acs = acompanhante_schema.AcompanhanteSchema()
        validate = acs.validate(request.json)

        if validate:
            make_response(jsonify(validate), 400)
        else:
            nome = request.json['nome']
            idade = request.json['idade']
            convidado = request.json['convidado_id']

            convidado_acompanhante = convidado_service.convidado_detail(convidado)
            if convidado_acompanhante is None:
                return make_response("Convidado não encontrado", 404)

            novo_acompanhante = acompanhante.Acompanhante(nome=nome, idade=idade, convidado=convidado_acompanhante)

            result = acompanhante_service.cadastrar_acompanhante(novo_acompanhante)

            return make_response(acs.jsonify(result), 201)
        
class AcompanhanteDetails(Resource):
    @jwt_required()
    def get(self, id):
        acompanhante = acompanhante_service.acompanhante_detail(id)
        if acompanhante is None:
            return make_response("Acompanhante não encontrado!", 404)
        
        acs = acompanhante_schema.AcompanhanteSchema()
        return make_response(acs.jsonify(acompanhante), 200)

    @jwt_required()
    def put(self, id):
        acompanhante_bd = acompanhante_service.acompanhante_detail(id)
        if acompanhante_bd is None:
            return make_response("Acompanhante não encontrado!", 404)
        
        acs = acompanhante_schema.AcompanhanteSchema()
        validate = acs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json['nome']
            idade = request.json['idade']
            convidado = acompanhante_bd.convidado
            acompanhante_novo = acompanhante.Acompanhante(nome=nome, idade=idade, convidado=convidado)

            acompanhante_service.editar_acompanhante(acompanhante_bd, acompanhante_novo)
            acompanhante_atualizado = acompanhante_service.acompanhante_detail(id)
            return make_response(acs.jsonify(acompanhante_atualizado), 200)

    @jwt_required()
    def delete(self, id):
        acompanhante = acompanhante_service.acompanhante_detail(id)
        if acompanhante is None:
            return make_response("Acompanhante não encontrado!", 404)
        
        acompanhante_service.remover_acompanhante(acompanhante)

        return make_response("", 204)

    
api.add_resource(Acompanhante, '/acompanhantes')
api.add_resource(AcompanhanteDetails, '/acompanhantes/<int:id>')