from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, String, Text, UUID
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()
