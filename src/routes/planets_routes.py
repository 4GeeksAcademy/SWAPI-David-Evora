from flask import jsonify, Blueprint
from models import Planet
from database import db
from sqlalchemy import select

planets = Blueprint("planets", __name__)

@planets.route("/planets", methods=["GET"])
def getPlanetsList():
    planets_list = []
    query = select(Planet)
    response = db.session.execute(query).scalars().all()
    
    if not response:
        return jsonify([]), 200
    
    for planet in response:
        planets_list.append({
            "id": planet.id,
            "name": planet.name    
        })
    
    return jsonify(planets_list), 200

@planets.route("/planets/<int:id>", methods=["GET"])
def getPlanet(id):
    response = db.session.execute(select(Planet).where(Planet.id == id)).scalar()

    if not response:
        return jsonify({"Error": "Planet not found"}), 404
    
    return jsonify(response.to_dict()), 200