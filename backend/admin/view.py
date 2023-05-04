from flask_admin.contrib.sqla import ModelView


class UserAdminView(ModelView):
    column_hide_backrefs = False
    column_list = ("roles", "city", "home", "street")