import os
import unittest

from app import app, db
from app.models import User,Ftasks
from config import basedir

from datetime import datetime,date

TEST_DB = 'test.db'

class TasksTest(unittest.TestCase):
	#setup db and teardown
	def setUp(self):
		app.config['TESTING'] = True
		app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(basedir, TEST_DB)
		self.app = app.test_client()
		db.create_all()

	def tearDown(self):
		db.drop_all()

	def login(self, username, password):
		return self.app.post('users/', data=dict(
			name = username,
			password = password), follow_redirects=True)

	def logout(self):
		return self.app.get('users/logout', follow_redirects=True)

	def register(self):
		return self.app.post('users/register/', data=dict(
			name = 'villancikos',
			email = 'villancikos@gmail.com',
			password = '123456',
			confirm='123456'), follow_redirects=True)

	def create_user(self):
		new_user = User('fulano','fulano@gmail.com','fulanote')
		db.session.add(new_user)
		db.session.commit()

	def create_task(self):
		return self.app.post('tasks/add')