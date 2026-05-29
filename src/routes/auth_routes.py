from flask import request, jsonify, Blueprint
from flask_jwt_extended import create_access_token
from sqlalchemy import select
from models import User
from database import db

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:
        return jsonify({"Error": "Username, password and email are required."}), 404
    
    existing_user = db.session.execute(select(User).where(User.username == username)).scalar()

    if existing_user:
        return jsonify({"Error": "Existing username"}), 409
    
    existing_email = db.session.execute(
        select(User).where(User.email == email)
    ).scalar()

    if existing_email:
        return jsonify({"Error": "Existing email"}), 409
    
    new_user = User(
        username = username,
        email = email,
        password = password
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"Message": "User created successfully."}), 201

@auth.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"Error": "Email and password are required."}), 404
    
    user = db.session.execute(select(User).where(User.email == email)).scalar()

    if not user or user.password != password:
        return jsonify({"Error": "Incorrect credentials."}), 401
    
    access_token = create_access_token(identity=str(user.id))

    return jsonify({
        "token": access_token,
        "user_id": user.id
    }), 200