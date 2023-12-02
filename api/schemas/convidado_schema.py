from api import ma
from ..schemas.acompanhante_schema import AcompanhanteSchema
from ..models import convidado_model
from marshmallow import fields

class ConvidadoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = convidado_model.Convidado
        fields = ('id', 'nome', 'telefone', 'casamento', 'acompanhantes')

    nome = fields.String(required=True)
    telefone = fields.String(required=True)
    casamento = fields.String(required=True)
    acompanhantes = fields.Nested(AcompanhanteSchema, only=('nome', 'idade'), many=True)