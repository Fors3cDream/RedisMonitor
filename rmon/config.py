import os

class DevConfig:
	DEBUG = True
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SQLALCHEMY_DATABASE_URI = 'sqlite://'
	TEMPATES_AUTO_RELOAD = True


class ProductConfig(DevConfig):

	DEBUG = False

	# sqlite data file path
	data_path = os.path.join(os.getcwd(), 'rmon.db').replace('\\', '/')
	SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(data_path)