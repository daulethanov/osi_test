import os
from flask import Blueprint, request, jsonify
from flask_uploads import UploadSet, IMAGES
from werkzeug.utils import secure_filename
from services.problem.model import ActJob, LevelProblem
from services.problem.model.problem import Problem
from services.problem.shema.problem import ProblemSchema
from services.problem.view import allowed_file

photos = UploadSet('photos', IMAGES)

problems = Blueprint('problems', __name__, url_prefix='/api/v1/problem')


@problems.route('/create', methods=['POST'])
def create_problem():
    file = request.files.get('file')

    # Проверка наличия файла и его расширения
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = photos.save(file)

        # Создание новой задачи с файлом
        problem = Problem(
            number=request.form.get('number'),
            telegram_name=request.form.get('telegram_name'),
            title=request.form.get('title'),
            description=request.form.get('description'),
            level_problem=request.form.get('level_problem', LevelProblem.minimal),
            file=file_path
        )

        problem.create_problem(problem)
        return {'message': 'File uploaded successfully'}

    return {'message': 'File upload failed'}, 400


@problems.route('/list', methods=["GET"])
def list_problem():
    problems = Problem.query.all()
    problem_schema = ProblemSchema(many=True)
    return jsonify(problem_schema.dump(problems))



