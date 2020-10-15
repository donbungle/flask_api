from models.user import UserModel

from ma import ma

class UserSchema(ma.Schema):
    class Meta:
        model = UserModel
        load_only = ("password",)
        dump_only = ("id",)
