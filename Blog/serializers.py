from rest_framework import serializers
from .models import BlogModel



class BlogModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = BlogModel
		fields = ('title', 'body', 'cover', 'created')