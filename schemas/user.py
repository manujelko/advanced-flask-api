from marshmallow import Schema, fields


class UserSchema(Schema):
    class Meta:
        load_only = ("password",)
        dumpy_only = ("id",)

    id = fields.Int()
    username = fields.Str(required=True)
    password = fields.Str(required=True)
