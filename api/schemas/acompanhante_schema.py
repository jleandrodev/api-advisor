from api import ma
from ..models import acompanhante_model
from marshmallow import fields

class AcompanhanteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = acompanhante_model.Acompanhante
        fields = ('id', 'nome', 'idade', 'convidado_id')
    
    nome = fields.String(required=True)
    idade = fields.String(required=True, validate=lambda s: s in [e.value for e in acompanhante_model.FaixaEtaria])
    
    convidado_id = fields.String(required=True)