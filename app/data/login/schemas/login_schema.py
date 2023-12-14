"""Schema for serializing/deserializing a login"""

from data.login.models.login_model import loginModel
from shared.utils.schema.base_schema import BaseSchema


class loginSchema(BaseSchema):
    class Meta:
        model = loginModel
        load_instance = True
