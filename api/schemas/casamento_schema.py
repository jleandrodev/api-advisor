from api import ma
from ..models import casamento_model
from marshmallow import fields

class CasamentoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = casamento_model.Casamento
        fields = ('id', 'name', 'data_casamento', 'assistentes', 'convidados')

    name = fields.String(required=True)
    data_casamento = fields.String(required=True)
    assistentes = fields.Nested('AssistenteSchema', only=('nome', 'telefone'), many=True)
    convidados = fields.Nested('ConvidadoSchema', only=('nome', 'telefone'), many=True)
