import jwt
import datetime


def create_access_token(id):
    return jwt.encode({
        'customer_id': id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=30),
        'iat': datetime.datetime.utcnow()
    }, 'access_secret', algorithm="HS256")


def create_refresh_token(id):
    return jwt.encode({
        'customer_id': id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=30),
        'iat': datetime.datetime.utcnow()
    }, 'refresh_secret', algorithm="HS256")
