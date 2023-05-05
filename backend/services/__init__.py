from flask import Flask
# from flask_cors import CORS
from flask_security import Security
from flask_migrate import Migrate
from flask_uploads import configure_uploads

from admin import admin
from config.base import Config
from flask_jwt_extended import JWTManager
from services.client.mail import mail
from services.client.model import db
from services.client.view.auth import auth
from services.problem.view.problem import problems, photos

migrate = Migrate(command='migrate')

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    configure_uploads(app, photos)

    Security(app)
    with app.app_context():
        db.create_all()
    mail.init_app(app)
    admin.init_app(app)
    JWTManager(app)
    app.register_blueprint(auth)
    app.register_blueprint(problems)
    # Cors(app, resources={r"*": {"origins": "*"}})

    return app
