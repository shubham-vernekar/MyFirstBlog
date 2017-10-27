from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=300)
	pub_date = models.DateTimeField()
	image = models.ImageField(upload_to='media/')
	body = models.TextField()

	def __str__(self):
		return self.title

	def pubDatePretty(self):
		return self.pub_date.strftime('%b %d %Y')

	def summary(self):
		if len(self.body)>100:
			return self.body[:250]+" ..."
		else:
			return self.body