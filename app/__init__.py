# app/__init__.py

# import packages
import os
from dotenv import load_dotenv
from flask import Flask
#from flask_cors import CORS

# Import routes
from app.models import db, migrate
from app.routes.flask_app import flask_app
from app.routes.recommend_routes import recommend_routes

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


def create_app():
    app = Flask(__name__)
    #CORS(app)

    #app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////mnt/c/Github/MediCabinet/data-engineering/database.sqlite3"
    # configure the database
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    migrate.init_app(app, db)

    # configure routes
    app.register_blueprint(flask_app)
    app.register_blueprint(recommend_routes)

    return app


if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
