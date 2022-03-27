from django.urls import path
from Blog.views import BlogListView, BlogModelListAPIView, blog_detail, popular_post



app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('api/', BlogModelListAPIView.as_view(), name='api'),

    path('detail/<int:pk>/', blog_detail, name='blog_detail'),
    path('popular/', popular_post, name='popular'),
]
