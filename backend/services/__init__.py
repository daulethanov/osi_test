from flask import Flask
from flask_cors import CORS
from flask_security import Security
from flask_migrate import Migrate
from admin import admin
from config.base import Config
from flask_jwt_extended import JWTManager
from services.client.mail import mail
from services.client.model import db
from services.client.view.auth import auth
from services.problem.view.problem import problems

migrate = Migrate(command='migrate', )


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    Security(app)
    mail.init_app(app)
    admin.init_app(app)
    JWTManager(app)
    CORS(app, resources={r"*": {"origins": "*"}})
    app.register_blueprint(auth)
    app.register_blueprint(problems)

    return app
