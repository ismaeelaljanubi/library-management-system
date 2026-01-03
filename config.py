import os
class Config:
    SECRET_KEY = "library-secret"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:0000@localhost/library_sys"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
   