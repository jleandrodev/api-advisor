from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flasgger import Swagger

app = Flask(__name__)

app.config.from_object('config')
db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
JWTManager(app)

api = Api(app)
swagger = Swagger(app)

from .views import casamento_view, convidado_view, assistente_view, usuario_view, login_view, acompanhante_view
from .models import casamento_model, convidado_model, assistente_model, usuario_model, acompanhante_model