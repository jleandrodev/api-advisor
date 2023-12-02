from flask_restful import Resource
from flask_jwt_extended import jwt_required
from api import api
from flask import request, make_response, jsonify
from ..schemas import convidado_schema
from ..entidades import convidado
from ..entidades.acompanhante import Acompanhante
from ..services import convidado_service, acompanhante_service

class ConvidadoList(Resource):
    @jwt_required()
    def get(self):
        convidados = convidado_service.listar_convidados()
        cs = convidado_schema.ConvidadoSchema(many=True)
        return make_response(cs.jsonify(convidados), 200)
    
    # @jwt_required()
    def post(self):
        cs = convidado_schema.ConvidadoSchema()
        validate = cs.validate(request.json)
        print(request.json)

        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome_convidado = request.json['nome']
            telefone_convidado = request.json['telefone']
            casamento_convidado = request.json['casamento']
            acompanhantes_data = request.json['acompanhantes']


            novo_convidado = convidado.Convidado(nome=nome_convidado, telefone=telefone_convidado, casamento=casamento_convidado, acompanhantes=acompanhantes_data)
            result = convidado_service.cadastrar_convidado(novo_convidado)
            
            for acompanhante in acompanhantes_data:
                nome_acompanhante = acompanhante["nome"]
                idade_acompanhante = acompanhante['idade']
                convidado_id = str(result.id)

                novo_acompanhante = Acompanhante(nome=nome_acompanhante, idade=idade_acompanhante, convidado=convidado_id)
                acompanhante_service.cadastrar_acompanhante(novo_acompanhante)

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
        
        cs = convidado_schema.ConvidadoSchemaInput()
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

    
api.add_resource(ConvidadoList, '/convidados')
api.add_resource(ConvidadoDetails, '/convidados/<int:id>')