from django.urls import path
from Blog.views import BlogListView, BlogModelListAPIView, PopularView, blog_detail



app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('api/', BlogModelListAPIView.as_view(), name='api'),

    path('<int:pk>/', PopularView.as_view(), name='popular'),
    path('detail/<int:pk>/', blog_detail, name='blog_detail'),
]
