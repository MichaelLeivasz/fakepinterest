from ProjetoFakePinterest import database, app
from ProjetoFakePinterest.models import Usuario, Foto

with app.app_context():
    database.drop_all()
    database.create_all()