from django.shortcuts import render

from  .models import BlogModel
from django.views.generic import ListView
from rest_framework.generics import ListAPIView
from .serializers import BlogModelSerializer


class BlogListView(ListView):
	template_name = 'layouts/base.html'
	model = BlogModel

	def get_queryset(self):
		blog = BlogModel.objects.all().order_by('-created')
		q = self.request.GET.get('q')
		if q:
			blog = BlogModel.objects.filter(title__icontains=q)

		return blog 


class BlogModelListAPIView(ListAPIView):
	queryset = BlogModel.objects.all()
	serializer_class = BlogModelSerializer

