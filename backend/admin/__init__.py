from flask_admin import Admin
from services.client.model.user import User, Role
from services.problem.model.problem import Problem, Rating
from services.client.model import db
from .view import UserAdminView
from flask_admin.contrib.sqla import ModelView


admin = Admin(name="OSI")


admin.add_view(UserAdminView(User, db.session))
admin.add_view(ModelView(Role, db.session))
admin.add_view(ModelView(Problem, db.session))
admin.add_view(ModelView(Rating, db.session))


