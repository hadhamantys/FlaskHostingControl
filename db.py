from flask import Flask
from flask_sqlalchemy import SQLAlchemy,BaseQuery
from flask_migrate import Migrate,MigrateCommand, Manager

app = Flask(__name__)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command("db",MigrateCommand)
