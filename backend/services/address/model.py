from services.client.model.user import db, User


class City(db.Model):
    __tablename__ = 'city'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    user = db.relationship('User', backref='cities')


class Street(db.Model):
    __tablename__ = 'street'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    user = db.relationship('User', backref='cities')


class Home(db.Model):
    __tablename__ = 'Home'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    user = db.relationship('User', backref='cities')

