from api import ma
from ..models import casamento_model
from marshmallow import fields

class CasamentoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = casamento_model.Casamento
        fields = ('id', 'name', 'data_casamento', 'convidados')

    name = fields.String(required=True)
    data_casamento = fields.String(required=True)
    convidados = fields.Nested('ConvidadoSchema', only=('id', 'nome', 'telefone', 'acompanhantes'), many=True)
