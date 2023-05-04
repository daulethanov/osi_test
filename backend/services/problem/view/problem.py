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

        filename = secure_filename(file.filename)
        from runserver import app
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        problem = Problem(**data, file=filename)
        problem.create_problem(problem)
        return jsonify({'message': 'Problem created successfully'}), 201
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400


@problems.route('/list', methods=["GET"])
def list_problem():
    pass
