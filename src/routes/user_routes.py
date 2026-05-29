from flask import jsonify, Blueprint
from flask_jwt_extended import get_jwt_identity, jwt_required
from models import User, Favorite
from database import db
from sqlalchemy import select

user = Blueprint("user", __name__)

@user.route("/users", methods=["GET"])
def getUsersList():
    users_list = []
    query = select(User)
    response = db.session.execute(query).scalars().all()

    if not response:
        return jsonify([]), 200
    
    for user in response:
        users_list.append({
            "id": user.id,
            "fullname": user.full_name,
            "username": user.username,
            "email": user.email,
            "created": user.created,
            "favorites": user.favorites
        })

    return jsonify(users_list)

@user.route("users/favorites", methods=["GET"])
@jwt_required()
def getUserFavorite():
    user_id = get_jwt_identity

    user = db.session.get(User, user_id)

    if not user:
        return jsonify({"Error": "User not found"})
    
    return jsonify([
        favorite.to_dict()
        for favorite in user.favorites
    ]), 200