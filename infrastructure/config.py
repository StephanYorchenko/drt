import os


class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'send_goge'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or "sqlite:///infrastucture/database.db"
	SQLALCHEMY_TRAK_MODIFICATIONS = False
