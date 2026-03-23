from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    user: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    photo: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    

class Comment(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    user_id: Mapped[int] = mapped_column(primary_key=True)
    post_id: Mapped[int] = mapped_column(primary_key=True)

    def serialize(self):
        return {
            "id": self.id,
            "text": self.text,
            # do not serialize the password, its a security breach
        }


class Dm(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    message: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    reciever_id: Mapped[int] = mapped_column(primary_key=True)
    sender_id: Mapped[int] = mapped_column(primary_key=True)

    def serialize(self):
        return {
            "id": self.id,
            "message": self.message,
            # do not serialize the password, its a security breach
        }
    
class Followers(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    seguido_id: Mapped[int] = mapped_column(primary_key=True)
    seguidores_id: Mapped[int] = mapped_column(primary_key=True)

    def serialize(self):
        return {
            "id": self.id,
            "seguido_id": self.seguido_id,
            # do not serialize the password, its a security breach
        }
    

class Post(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    publicacion: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    user_id: Mapped[int] = mapped_column(primary_key=True)

    def serialize(self):
        return {
            "id": self.id,
            "message": self.message,
            # do not serialize the password, its a security breach
        }

