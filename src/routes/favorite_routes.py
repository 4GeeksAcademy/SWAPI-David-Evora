from flask import jsonify, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy import select
from models import Favorite, User, Planet, People
from database import db

favorite = Blueprint("favorite", __name__)

@favorite.route("/favorite/planet/<int:planet_id>", methods=["POST"])
@jwt_required()
def addFavoritePlanet(planet_id):
    user_id = get_jwt_identity()

    user = db.session.get(User, user_id)

    if not user:
        return jsonify({"Error": "User not found"}), 404

    planet = db.session.get(Planet, planet_id)

    if not planet:
        return jsonify({"Error": "Planet not found"}), 404    
    
    new_favorite = Favorite(
        user_id= user.id,
        planet_id= planet.id
    )

    db.session.add(new_favorite)
    db.session.commit()

    return jsonify(new_favorite.to_dict()), 201

@favorite.route("/favorite/people/<int:people_id>", methods=["POST"])
@jwt_required()
def addFavoritePeople(people_id):
    user_id = get_jwt_identity()

    user = db.session.get(User, user_id)

    if not user:
        return jsonify({"Error": "User not found"}), 404
    
    people = db.session.get(People, people_id)

    if not people:
        return jsonify({"Error": "People not found"}), 404
    
    new_favorite = Favorite(
        user_id= user.id,
        people_id= people.id
    )

    db.session.add(new_favorite)
    db.session.commit()

    return jsonify(new_favorite.to_dict()), 201

@favorite.route("/favorite/planet/<int:planet_id>", methods=["DELETE"])
@jwt_required()
def rmFavoritePlanet(planet_id):
    user_id = get_jwt_identity()

    favorite = db.session.execute(select(Favorite).where(
        Favorite.user_id == user_id,
        Favorite.planet_id == planet_id
    )).scalar()

    if not favorite:
        return jsonify({"Error": "Favorite not found"}), 404

    db.session.remove(favorite)
    db.session.commit()

    return jsonify({"Success": "Favorite deleted"}), 200

@favorite.route("/favorite/people/<int:people_id>", methods=["DELETE"])
@jwt_required()
def rmFavoritePeople(people_id):
    user_id = get_jwt_identity()

    favorite = db.session.execute(select(Favorite).where(
        Favorite.user_id == user_id,
        Favorite.people_id == people_id
    )).scalar()

    if not favorite:
        return jsonify({"Error": "Favorite not found"}), 404

    db.session.remove(favorite)
    db.session.commit()

    return jsonify({"Success": "Favorite deleted"}), 200