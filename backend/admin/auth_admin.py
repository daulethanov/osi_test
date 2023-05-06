from flask import request, g, make_response
from flask_admin import expose, AdminIndexView


class MyAdminView(AdminIndexView):
    """Handle admin login"""

    @expose('/', methods=['POST', 'GET'])
    def index(self):
        if request.cookies.get('ok') == 'man':
            return super(MyAdminView, self).index()

        if (request.form
            and request.form.get('username') == 'admin'
            and request.form.get('password') == 'admin_password'):
            g.ok = True

            response = make_response(super(MyAdminView, self).index())
            response.set_cookie('ok', 'man')
            return response

        return """
        <form method="POST">
        <input type="text" name="username">
        <input type="password" name="password">
        <input type="submit" value="Login">
        </form>
        """