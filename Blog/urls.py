
from django.urls import path
from Blog.views import BlogListView, BlogModelListAPIView



app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('api/', BlogModelListAPIView.as_view(), name='api'),
]
