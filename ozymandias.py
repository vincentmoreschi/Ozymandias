import os
from app import create_app, db
#from app.models import User, Role
from flask_migrate import Migrate

app = create_app('default')
migrate = Migrate(app, db)
