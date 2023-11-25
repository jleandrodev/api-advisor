from api import ma
from ..models import assistente_model
from marshmallow import fields

class AssistenteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = assistente_model.Assistente
        fields = ('id', 'nome', 'telefone', 'casamentos')
    
    nome = ma.auto_field(required=True)
    telefone = ma.auto_field(required=True)
    casamentos = ma.auto_field()