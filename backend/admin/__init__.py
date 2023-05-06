from flask_admin import Admin
from services.client.model.user import User, Role
from services.problem.model.problem import Problem, Rating
from services.client.model import db
from .view import UserAdminView, ProblemView
from flask_admin.contrib.sqla import ModelView
from services.address.model import City, Street, Home
from .auth_admin import MyAdminView


admin = Admin(name="OSI", template_mode="bootstrap3", index_view=MyAdminView())


admin.add_view(UserAdminView(User, db.session))
admin.add_view(ModelView(Role, db.session))
admin.add_view(ProblemView(Problem, db.session))
admin.add_view(ModelView(Rating, db.session))
admin.add_view(ModelView(Home, db.session))
admin.add_view(ModelView(Street, db.session))
admin.add_view(ModelView(City, db.session))


