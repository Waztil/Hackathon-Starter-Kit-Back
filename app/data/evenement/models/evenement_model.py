from sqlalchemy import Column, String, Integer

from shared import db


class evenementModel(db.Model):
    __tablename__ = "evenement"
    id = Column(
        Integer,
        primary_key=True,
        unique=True,
        nullable=False
    )