from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin

class CustomUser(AbstractUser):
	POST_CHOICES = [('SeniorCoordinator','SeniorCoordinator'), ('JuniorCoordinator','JuniorCoordinator'), ('BoardMember','BoardMember')]
	post = models.CharField(max_length = 18,
								choices=POST_CHOICES,
								default='JuniorCoordinator')
	email = models.EmailField(unique=True)
	# we will allow access to our website only to staff members

	REQUIRED_FIELDS = ['email',	]
