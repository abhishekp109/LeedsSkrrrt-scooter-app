from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
# Handles all migrations.
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)


# Do not put the import code below at top of file. This is to avoid circular dependencies.
from app import views, models
