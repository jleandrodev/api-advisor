debug = True

USERNAME = 'root'
PASSWORD = 'localhost123'
SERVER = 'localhost'
DB = 'app_advisor'

SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'api-advisor'