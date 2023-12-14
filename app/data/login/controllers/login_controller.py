""" Routes for the endpoint 'login'"""

from flask import Blueprint, request
from marshmallow import ValidationError

from data.login.models import loginModel
from data.login.schemas import loginSchema
from shared import db

NAME = 'login'

login_blueprint = Blueprint(f"{NAME}_login_blueprint", __name__)


@login_blueprint.get(f"/login/<int:id>")
def get_hlogin(id: str):
    """GET route code goes here"""
    entity: loginModel = db.session.query(loginModel).get(id)

    # Vérifier si l'entité (utilisateur) a été trouvée
    if not entity:
        return "Utilisateur non trouvé", 404

    payload = request.get_json()
    mot_de_passe_fourni = payload.get('mot_de_passe')
    
    # Vérifier si le mot de passe fourni correspond au mot de passe enregistré en base de données
    if entity.mot_de_passe == mot_de_passe_fourni:
        return "Vous êtes connecté", 200
    else:
        return "Mot de passe incorrect", 401


@login_blueprint.post(f"/login")
def post_login():
    """POST route code goes here"""
    payload = request.get_json()
    try:
        entity: loginModel = loginSchema().load(payload)
    except ValidationError as error:
        return f"The payload does't correspond to a valid loginModel: {error}", 400
    db.session.add(entity)
    db.session.commit()
    return loginSchema().dump(entity), 200


@login_blueprint.delete(f"/login/<int:id>")
def delete_login(id: str):
    """DELETE route code goes here"""
    return "Unimplemented", 501


@login_blueprint.put(f"/login/<int:id>")
def put_login(id: str):
    """PUT route code goes here"""
    return "Unimplemented", 501


@login_blueprint.patch(f"/login/<int:id>")
def patch_login(id: str):
    """PATCH route code goes here"""
    return "Unimplemented", 501
