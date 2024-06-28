import os


class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'mysql://root:2332@localhost/distribuidora_legal'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
