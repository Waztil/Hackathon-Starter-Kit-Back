""" Routes for the endpoint 'evenement'"""

from flask import Blueprint, request
from marshmallow import ValidationError

from data.evenement.models import evenementModel
from data.evenement.schemas import evenementSchema
from shared import db

NAME = 'evenement'

evenement_blueprint = Blueprint(f"{NAME}_evenement_blueprint", __name__)


@evenement_blueprint.get(f"/evenement/<int:id>")
def get_evenement(id: str):
    """GET route code goes here"""
    entity: evenementModel = db.session.query(evenementModel).get(id)
    if entity is None:
        return "evenement", 404
    return entity.message, 200


@evenement_blueprint.post(f"/evenement/")
def post_evenement():
    """POST route code goes here"""
    payload = request.get_json()
    try:
        entity: evenementModel = evenementSchema().load(payload)
    except ValidationError as error:
        return f"The payload does't correspond to a valid evenementModel: {error}", 400
    db.session.add(entity)
    db.session.commit()
    return evenementSchema().dump(entity), 200


@evenement_blueprint.delete(f"/evenement/<int:id>")
def delete_evenement(id: str):
    """DELETE route code goes here"""
    return "Unimplemented", 501


@evenement_blueprint.put(f"/evenement/<int:id>")
def put_evenement(id: str):
    """PUT route code goes here"""
    return "Unimplemented", 501


@evenement_blueprint.patch(f"/evenement/<int:id>")
def patch_evenement(id: str):
    """PATCH route code goes here"""
    return "Unimplemented", 501
