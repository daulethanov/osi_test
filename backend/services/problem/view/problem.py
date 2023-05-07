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
    file = request.files.get('file')

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
            name=request.form.get('title'),
			surname=request.form.get('title'),
			whatsapp=request.form.get('title'),
			address = request.form.get('address')
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


@problems.route('/edit/<int:id>', methods=["PUT"])
def edit_problem(id):
    problem = Problem.query.filter_by(id=id).first()
    data = ProblemSchema(only=("id", "act_job",)).load(request.json)
    if not problem:
        return jsonify({'message': 'Problem not found'}), 404
    problem.act_job = data["act_job"]
    db.session.commit()
    return ProblemSchema().dump(problem)



