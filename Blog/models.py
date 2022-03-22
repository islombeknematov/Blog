from django.db import models
from django.contrib.auth.models import User

		
class CategoryModel(models.Model):
	title = models.CharField(max_length=20, null=True, blank=True)


	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'category'
		verbose_name_plural = 'categories'


class BlogModel(models.Model):
	title = models.CharField(max_length=50, null=True, blank=True)
	body = models.TextField()
	cover = models.ImageField(upload_to='media', null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

	categories = models.ForeignKey(CategoryModel, on_delete=models.PROTECT,
								 default=1, related_name='blogs')

	popular = models.ManyToManyField(User, blank=True, related_name='popular')

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'blog'
		verbose_name_plural = 'blogs'





