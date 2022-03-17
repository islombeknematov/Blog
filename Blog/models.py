from django.db import models

# Create your models here.


class BlogModel(models.Model):
	title = models.CharField(max_length=50, null=True, blank=True)
	body = models.TextField()
	cover = models.ImageField(upload_to='media', null=True, blank=True)

	created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'blog'
		verbose_name_plural = 'blogs'

		