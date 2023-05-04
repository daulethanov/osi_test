from services.client.model.user import db, User


class City(db.Model):
    __tablename__ = 'city'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    user_id = db.relationship(User, backref=db.backref('cities'))

    def __repr__(self):
        return self.name


class Street(db.Model):
    __tablename__ = 'street'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    user_id = db.relationship(User, backref=db.backref('streets'))

    def __repr__(self):
        return self.name


class Home(db.Model):
    __tablename__ = 'home'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    user_id = db.relationship(User, backref=db.backref('homes'))

    def __repr__(self):
        return self.name
