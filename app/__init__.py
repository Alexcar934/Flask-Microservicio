from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import json

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Cargar configuración desde variables de entorno (Docker) o valores por defecto
    DB_USER = os.environ.get("DB_USER", "mbit")
    DB_PASSWORD = os.environ.get("DB_PASSWORD", "mbit")
    DB_HOST = os.environ.get("DB_HOST", "db")  # nombre del contenedor en docker-compose
    DB_NAME = os.environ.get("DB_NAME", "Pictures")

    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Importar y registrar vistas (endpoints)
    from .views import api_blueprint
    app.register_blueprint(api_blueprint)

    return app
