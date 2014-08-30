import os

# grabs the folder where the script runs
# abspath returns an absolute path
# I believe os.path.dirname(__FILE__) returns this file's path
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
CSRF_ENABLED = True
SECRET_KEY = 'my_precious'

# defines the full path for the database 
DATABASE_PATH = os.path.join(basedir,DATABASE)

# the database uri
SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ DATABASE_PATH