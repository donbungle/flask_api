DEBUG = True

SQLALCHEMY_DATABASE_URI = "postgresql://postgres:1q2w3e4r5t@postgres:5432/FLASK_API"
#SQLALCHEMY_DATABASE_URI = "postgresql://postgres:1q2w3e4r5t@127.0.0.1:6002/FLASK_API"

SQLALCHEMY_TRACK_MODIFICATIONS = False
PROPAGATE_EXCEPTIONS = True
SECRET_KEY = "change-this-key-in-the-application-config"
JWT_SECRET_KEY = "change-this-key-to-something-different-in-the-application-config"
    