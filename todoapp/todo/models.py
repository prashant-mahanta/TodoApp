from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TodoApp(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='all_todos')
	heading = models.CharField(max_length=20, blank=False, null=False)
	description = models.TextField()
	schedule = models.DateTimeField(default=None, blank=False, null=False)
	status = models.CharField(default="no", max_length=10)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.heading
