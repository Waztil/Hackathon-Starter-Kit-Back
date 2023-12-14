from sqlalchemy import Column, String, Integer

from shared import db


class loginModel(db.Model):
    tablename = "Utilisateurs"
    id_utilisateur = Column (
        Integer,
        primary_key=True,
        unique=True,
        autoincrement=True,
    )

    pseudo = Column (
        String(255),
        nullable=False,
    )

    mot_de_passe = Column (
        String(255),
        nullable=False,
    )