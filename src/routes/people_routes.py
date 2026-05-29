from flask import jsonify, Blueprint
from models import People
from database import db
from sqlalchemy import select

people = Blueprint("people", __name__)

@people.route("/people", methods=["GET"])
def getPeopleList():
    people_list = []
    query = select(People)
    response = db.session.execute(query).scalars().all()

    if not response:
        return jsonify([]), 200
    
    for person in response:
        people_list.append({
            "id": person.id,
            "name": person.name
        })

    return jsonify(people_list), 200

@people.route("/people/<int:id>", methods=["GET"])
def getPeople(id):
    person = db.session.execute(select(People).where(People.id == id)).scalar()

    if not person:
        return jsonify({"Error": "People not found"}), 404
    
    return jsonify(person.to_dict()), 200