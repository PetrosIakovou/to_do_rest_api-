from extensions import db
from sqlalchemy.orm import Mapped
from werkzeug.security import generate_password_hash, check_password_hash
from uuid import uuid4

class Users(db.Model):
    __tablename__ = "users"

    id: Mapped[uuid4] = db.mapped_column(db.String(), primary_key=True, default = str(uuid4()))
    username: Mapped[str] = db.mapped_column(db.String(), nullable=False)
    email: Mapped[str] = db.mapped_column(db.String(), nullable=False)
    password: Mapped[str] = db.mapped_column(db.Text())


    def __repr__(self):
        return f"<User {self.username}>"
    
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    @classmethod
    def get_user_by_username(cls,username):
        return cls.query.filter_by(username= username).first()
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    