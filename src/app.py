import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from database import db
from routes.auth_routes import auth
from routes.user_routes import user
from routes.planets_routes import planets
from routes.people_routes import people
from routes.favorite_routes import favorites

app = Flask(__name__)
jwt = JWTManager(app)

app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")

if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["JWT_SECRET_KEY"] = "super-secret-key"

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)

app.register_blueprint(auth)
app.register_blueprint(user)
app.register_blueprint(people)
app.register_blueprint(planets)
app.register_blueprint(favorites)

setup_admin(app)

@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

@app.route('/')
def sitemap():
    return generate_sitemap(app)

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
