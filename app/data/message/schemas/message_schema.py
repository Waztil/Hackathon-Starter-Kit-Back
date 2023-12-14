"""Schema for serializing/deserializing a messageModel"""

from data.message.models.message_model import messageModel
from shared.utils.schema.base_schema import BaseSchema


class messageSchema(BaseSchema):
    class Meta:
        model = messageModel
        load_instance = True
