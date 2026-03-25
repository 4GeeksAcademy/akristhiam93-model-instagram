from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean,ForeignKey
from sqlalchemy.orm import Mapped, mapped_column,relationship
from typing import List

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    user: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    photo: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(String(240), nullable=False)
    password: Mapped[str] = mapped_column(nullable=True)
    
    posts: Mapped[List["Post"]] = relationship(back_populates="user")

    followers: Mapped[List["Followers"]] = relationship(back_populates="user")

    dms: Mapped[List["Dm"]] = relationship(back_populates="user")

    comments: Mapped[List["Comment"]] = relationship(back_populates="user")


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    

class Comment(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(String(120), nullable=False)
    user_id: Mapped[int] = mapped_column(unique=True)
    post_id: Mapped[int] = mapped_column(unique=True)

    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))
    post: Mapped["User"] = relationship(back_populates="comments")

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["Parent"] = relationship(back_populates="comments")

    def serialize(self):
        return {
            "id": self.id,
            "text": self.text,
            # do not serialize the password, its a security breach
        }


class Dm(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    message: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    reciever_id: Mapped[int] = mapped_column(nullable=False)
    sender_id: Mapped[int] = mapped_column(nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="dms")

    def serialize(self):
        return {
            "id": self.id,
            "message": self.message,
            # do not serialize the password, its a security breach
        }
    
class Followers(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    seguido_id: Mapped[int] = mapped_column(unique=True, nullable=False)
    seguidores_id: Mapped[int] = mapped_column(unique=True, nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="followers")

    def serialize(self):
        return {
            "id": self.id,
            "seguido_id": self.seguido_id,
            # do not serialize the password, its a security breach
        }
    

class Post(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    publicacion: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="posts")
    
    comment: Mapped[List["Comment"]] = relationship(back_populates="post")


    def serialize(self):
        return {
            "id": self.id,
            "message": self.message,
            # do not serialize the password, its a security breach
        }

