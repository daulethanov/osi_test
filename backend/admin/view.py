import os
from flask_admin.form import FileUploadField
from flask_admin.contrib.sqla import ModelView
from flask_wtf.file import FileRequired
from werkzeug.utils import secure_filename
from wtforms.fields import FileField


class ProblemView(ModelView):
    column_list = ['id', 'create_at',]
    form_overrides = dict(file=FileField)
    form_args = dict(
        file=dict(validators=[FileRequired()])
    )
    form_extra_fields = {
        'file': FileUploadField('Image')
    }

    def on_model_change(self, form, model, is_created):

        file = form.file.data
        if file:
            filename = secure_filename(file.filename)
            model.file = file.read()
            file.seek(0, os.SEEK_END)
            model.file_size = file.tell()


class UserAdminView(ModelView):
    column_hide_backrefs = False
    column_list = ("roles", "city", "home", "street")

