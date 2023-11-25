from api import ma
from ..models import assistente_model
from marshmallow import fields

class LoginSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = assistente_model.Assistente
        fields = ('id', 'nome', 'email', 'senha')
    
    nome = fields.String(required=False)
    email = fields.String(required=True)
    senha = fields.String(required=True)