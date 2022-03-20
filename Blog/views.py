from django.shortcuts import render, get_object_or_404

from  .models import BlogModel, CategoryModel
from django.views.generic import ListView
from rest_framework.generics import ListAPIView
from .serializers import BlogModelSerializer


class BlogListView(ListView):
	template_name = 'layouts/base.html'
	model = BlogModel 

	def get_context_data(self, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context['categories'] = CategoryModel.objects.all()

		return context


	def get_queryset(self):
		blog = BlogModel.objects.order_by('-created')	#[:4]

		q = self.request.GET.get('q')
		if q:
			blog = blog.filter(title__icontains=q)

		category = self.request.GET.get('category')

		if category:
			blog = blog.filter(categories__pk=category)

		categories = CategoryModel.objects.all()

		return blog



class BlogModelListAPIView(ListAPIView):
	queryset = BlogModel.objects.all()
	serializer_class = BlogModelSerializer

