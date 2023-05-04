from flask import Blueprint, jsonify, request
from marshmallow import ValidationError
from services.client.mail import send_password_reset_email
from services.client.model.user import User, db
from services.client.shema.user import UserSchema
from flask_jwt_extended import jwt_required, get_jwt_identity

auth = Blueprint('auth', __name__, url_prefix='/api/v1/auth')


@auth.route('/register', methods=['POST'])
def register():
    try:
        user_data = UserSchema(only=('email', 'password')).load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    pwd = User.password_hash(password=user_data['password'])

    user = User(
        email=user_data['email'],
        password=pwd
    )
    user.create_users(user)
    result = UserSchema().dump(user)
    return jsonify(result), 201


@auth.route('/login', methods=["POST"])
def login():
    try:
        user_data = UserSchema(only=('email', 'password')).load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    user = User.query.filter_by(email=user_data['email']).first()
    if user:
        access_token = user.create_token(email=(user_data['email']), identity=user.id, id=user.id)

        return jsonify({"access_token": access_token,
                        "user": user.id})
    else:
        return jsonify(message="Invalid email or password"), 401


@auth.route("/account", methods=["GET"])
@jwt_required()
def me_account():
    user_id = get_jwt_identity()
    user = User.query.filter_by(id=user_id).first()

    if not user:
        return jsonify({
            "message": "Вы ввели неверный пароль"
        }), 403
    else:
        return jsonify({
            "user_id": user.id,
            "email": user.email,
            "created_at": user.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }), 200


@auth.route('/reset_password', methods=["POST"])
def reset_password():
    try:
        user_data = UserSchema(only=('email', )).load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 200

    user = User.query.filter_by(email=user_data['email']).first()

    if user:
        code = user.create_reset_password_code()
        send_password_reset_email(user, code)
        return jsonify("Сообщения отправлено"), 200

    else:
        return jsonify({"message": "Нету такого email"})


@auth.route("/reset_password/confirm", methods=["POST"])
def reset_password_confirm():
    try:
        user_data = UserSchema(only=('reset_password_code', 'password')).load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 200

    user = User.query.filter_by(reset_password_code=user_data['reset_password_code']).first()

    if user:
        user.reset_password_code = None
        user.password = user_data['password']
        db.session.add(user)
        db.session.commit()
        return jsonify({
            "message": "Вы изменили пароль"
        }), 200

    else:
        return jsonify({
            "Не верный код"
        }), 200


