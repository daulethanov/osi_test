from datetime import datetime

from services.client.model import db
from services.problem.model import ActJob


class Problem(db.Model):
    __tablename__ = 'problem'

    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    title = db.Column(db.Text())
    description = db.Column(db.Text())
    create_at = db.Column(db.DateTime(), default=datetime.now())
    finish = db.Column(db.DateTime())
    completed = db.Column(db.Boolean(), default=0)
    act_job = db.Column(db.Enum(ActJob), default=ActJob.pending)
    file = db.Column(db.LargeBinary)
    rating = db.relationship('Rating', backref='problem')

    def create_problem(self, problem):
        db.session.add(problem)
        db.session.commit()

    def general_rating(self):
        if not self.rating:
            return 0.0
        else:
            return sum(r.star for r in self.ratings) / len(self.ratings)


class Rating(db.Model):
    __tablename__ = 'rating'

    id = db.Column(db.Integer(), primary_key=True)
    problem_id = db.Column(db.Integer(), db.ForeignKey('problem.id'))
    star = db.Column(db.Float())
    create_at = db.Column(db.DateTime(), default=datetime.now())


