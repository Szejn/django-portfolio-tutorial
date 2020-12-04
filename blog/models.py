from django.db import models

class Blog(models.Model):
	title = models.CharField(max_length=200)
	date = models.DateField()
	body = models.TextField()

	def __str__(self):
		return self.title