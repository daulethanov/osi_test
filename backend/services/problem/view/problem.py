import os
from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from werkzeug.utils import secure_filename
from services.problem.model.problem import Problem
from services.problem.shema.problem import ProblemSchema

problems = Blueprint('problems', __name__, url_prefix='/api/v1/problem')


@problems.route('/create', methods=['POST'])
def create_problem():
    try:
        data = ProblemSchema().load(request.form)
        file = request.files['file']
        if not file:
            return {'message': 'No file uploaded'}, 400
        from runserver import app

        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        with app.app_context():
            data['file'] = filename  # добавляем имя файла в данные
            problem = Problem(**data)
            problem.create_problem(problem)

        return jsonify({'message': 'Problem created successfully'}), 201
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400


@problems.route('/list', methods=["GET"])
def list_problem():
    problems = Problem.query.all()
    problem_schema = ProblemSchema(many=True)
    return jsonify(problem_schema.dump(problems))



