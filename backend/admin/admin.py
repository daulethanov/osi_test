from flask_admin.contrib.sqla import ModelView
from services.client.model.user import User, Role, db
from . import admin
from .view import UserAdminView


admin.add_view(UserAdminView(User, db.session))




