""" Routes for the endpoint 'message'"""

from flask import Blueprint, request
from marshmallow import ValidationError

from data.message.models import messageModel
from data.message.schemas import messageSchema
from shared import db

NAME = 'message'

message_blueprint = Blueprint(f"{NAME}_message_blueprint", __name__)


@message_blueprint.get(f"/message/<int:id>")
def get_message(id: str):
    """GET route code goes here"""
    entity: messageModel = db.session.query(messageModel).get(id)
    if entity is None:
        return "message", 404
    return entity.message, 200


@message_blueprint.post(f"/message/")
def post_message():
    """POST route code goes here"""
    payload = request.get_json()
    try:
        entity: messageModel =messageSchema().load(payload)
    except ValidationError as error:
        return f"The payload does't correspond to a valid messageModel: {error}", 400
    db.session.add(entity)
    db.session.commit()
    return messageSchema().dump(entity), 200


@message_blueprint.delete(f"/message/<int:id>")
def delete_message(id: str):
    """DELETE route code goes here"""
    return "Unimplemented", 501


@message_blueprint.put(f"/message/<int:id>")
def put_message(id: str):
    """PUT route code goes here"""
    return "Unimplemented", 501


@message_blueprint.patch(f"/message/<int:id>")
def patch_message(id: str):
    """PATCH route code goes here"""
    return "Unimplemented", 501
