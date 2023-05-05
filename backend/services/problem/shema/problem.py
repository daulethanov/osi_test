from datetime import datetime
from marshmallow import Schema, fields as f
from services.client.shema.user import UserSchema
from services.problem.model import ActJob


class ProblemSchema(Schema):
    id = f.Integer(dump_only=True)
    # user_id = f.Nested(UserSchema(dump_only=('id', 'first_name', 'last_name', 'number'), many=True))
    telegram_name = f.String()
    number = f.Integer()
    title = f.String()
    description = f.String()
    create_at = f.DateTime(default=datetime.now, dump_only=True)
    finish = f.DateTime()
    completed = f.Bool(default=0)
    act_job = f.Enum(ActJob, default=ActJob.pending)
    rating = f.Nested('RatingSchema', dump_only=('id', 'star'), many=True)
    file = f.Raw()


class RatingSchema(Schema):
    id = f.Integer(dump_only=True)
    problem_id = f.Nested(ProblemSchema(only=('rating', 'id')))
    star = f.Float()
    create_at = f.DateTime(default=datetime.now())

