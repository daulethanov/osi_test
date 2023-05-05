from random import randrange
from . import db
from datetime import datetime, timedelta
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_security import SQLAlchemySessionUserDatastore, RoleMixin, UserMixin
from werkzeug.security import generate_password_hash


class Role(db.Model, RoleMixin):
    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(200))

    def __repr__(self):
        return self.name


class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    token = db.Column(db.BigInteger(), unique=True)
    active = db.Column(db.Boolean(), default=1)
    created_at = db.Column(db.DateTime, default=datetime.now())
    number = db.Column(db.Integer(), default=8)
    reset_password_code = db.Column(db.Integer())
    roles = db.relationship('Role', secondary='roles_users', backref=db.backref('users', lazy='dynamic'))
    # problem = db.relationship('Problem', backref=db.backref('users'))
    city = db.Column(db.Integer(), db.ForeignKey('city.id'))
    street = db.Column(db.Integer(), db.ForeignKey('street.id'))
    home = db.Column(db.Integer(), db.ForeignKey('home.id'))

    def __repr__(self):
        return self.email

    def password_hash(password):
        return generate_password_hash(password)

    def create_users(self, user):
        db.session.add(user)
        db.session.commit()

    def create_token(self, identity, email, id):
        return create_access_token(identity=identity, additional_claims={"email": email,
                                                                         "user_id": id})

    def refresh_token(self):
        token = create_refresh_token(
            identity=self.id
        )
        return token

    def create_reset_password_code(self):
        code = randrange(100000, 999999)
        self.reset_password_code = code
        db.session.commit()
        return code


roles_users = db.Table(
    'roles_users',
    db.Column('id', db.Integer, primary_key=True, autoincrement=True),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
)


user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)
