from models.user import UserModel

from ma import ma

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        load_instance = True
        load_only = ("password",)
        dump_only = ("id",)
