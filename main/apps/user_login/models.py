from __future__ import unicode_literals
from django.db import models

class UserManager(models.Manager):
	def basic_validator(self, postData):
		errors = {}
		if len(postData['first_name']) < 1:
			errors['first_name'] = "First name must contain more than one character"
		if len(postData['last_name']) < 1:
			errors['last_name'] = "Last name must contain more than one character"
		if len(postData['email']) < 5:
			errors['email'] = "Please enter a valid email address"
		return errors	
				

class User(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=150)
	email = models.EmailField(max_length=254)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()

	def __repr__(self):
		return "<User: %s>" % self.first_name