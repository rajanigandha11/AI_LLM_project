from django.db import models

class Blog(models.Model):
	title=models.CharField(max_length=200)
	discription=models.TextField()
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now_add=True)
	author=models.CharField(max_length=100)

	def __str__(self):
		return self.title
