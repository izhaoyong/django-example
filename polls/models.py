from django.db import models

# Create your models here.


class BookInfo(models.Model):
	def __str__(self):
		return self.author


	id = models.AutoField(primary_key=True)
	source_id = models.CharField(max_length=100)
	create_time = models.DateTimeField(auto_now=True)
	author = models.CharField(max_length=50)
	info = models.TextField()

	class Meta:
		app_label = 'polls'
