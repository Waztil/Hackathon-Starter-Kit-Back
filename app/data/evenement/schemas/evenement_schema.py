"""Schema for serializing/deserializing a evenementModel"""

from data.evenement.models.evenement_model import evenementModel
from shared.utils.schema.base_schema import BaseSchema


class evenementSchema(BaseSchema):
    class Meta:
        model = evenementModel
        load_instance = True
