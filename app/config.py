import os
import sys

EXEC_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))
class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Som3$ec5etK*y'
    UPLOAD_FOLDER = './uploads'
    SQLALCHEMY_DATABASE_URI='postgres://xdgvzjdrkqaesj:7628fb6ce1c9c45bb35250ab7a823111443d2552e0782bfb15b2a477323190c1@ec2-18-214-208-89.compute-1.amazonaws.com:5432/d5dtdifq01uj6h'
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed
    
    if os.path.isdir(UPLOAD_FOLDER) is False:
            os.mkdir(UPLOAD_FOLDER)
            
class DevelopmentConfig(Config):
    """Development Config that extends the Base Config Object"""
    DEVELOPMENT = True
    DEBUG = True

class ProductionConfig(Config):
    """Production Config that extends the Base Config Object"""
    DEBUG = False
