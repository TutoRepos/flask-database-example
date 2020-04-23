
class Config:

    #general config
    FLASK_APP = 'wsgi.py'
   
    # database config
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
