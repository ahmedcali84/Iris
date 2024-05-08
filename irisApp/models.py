from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
	pass

class IrisModel(models.Model):
	user = models.ForeignKey("User", on_delete=models.CASCADE , related_name='flowers')
	sepal_length = models.FloatField()
	sepal_width  = models.FloatField()
	petal_length = models.FloatField()
	petal_width = models.FloatField()
	prediction = models.CharField(max_length=12)

	def serialize(self):
		return {
			"user": self.user.username,
			"id": self.id,
			"sepal_length":self.sepal_length,
			"sepal_width": self.sepal_width,
			"petal_length":self.petal_length,
			"petal_width": self.petal_width,
			"prediction": self.prediction
		}


