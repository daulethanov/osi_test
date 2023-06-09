from flask import Blueprint, request, jsonify
from flask_uploads import UploadSet, IMAGES
from werkzeug.utils import secure_filename
from services.problem.model import LevelProblem
from services.problem.model.problem import Problem, db
from services.problem.shema.problem import ProblemSchema
from services.problem.view import allowed_file

photos = UploadSet('photos', IMAGES)

problems = Blueprint('problems', __name__, url_prefix='/api/v1/problem')


@problems.route('/create', methods=['POST'])
def create_problem():
    try:
        # Валидация данных запроса
        data = ProblemSchema().load(request.json)
    except ValidationError as e:
        return jsonify({'error': e.messages}), 400

    problem = Problem(
        number=data['number'],
        telegram_name=data['telegram_name'],
        title=data['title'],
        description=data['description'],
        # level_problem=data['level_problem'],
        name=data['name'],
        surname=data['surname'],
        whatsapp=data['whatsapp'],
        address=data['address'],
    )
    db.session.add(problem)
    db.session.commit()

    # Возврат данных созданной проблемы в ответе
    result = ProblemSchema().dump(problem)
    return jsonify(result), 201


@problems.route('/list', methods=["GET"])
def list_problem():
    problems = Problem.query.all()
    problem_schema = ProblemSchema(many=True)
    return jsonify(problem_schema.dump(problems))


@problems.route('/edit/<int:id>', methods=["PUT"])
def edit_problem(id):
    problem = Problem.query.filter_by(id=id).first()
    data = ProblemSchema(only=("id", "act_job",)).load(request.json)
    if not problem:
        return jsonify({'message': 'Problem not found'}), 404
    problem.act_job = data["act_job"]
    db.session.commit()
    return ProblemSchema().dump(problem)



