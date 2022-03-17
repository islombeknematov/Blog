from django.conf import settings 
from django.conf.urls.static import static 

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', include('Contact.urls', namespace='contact')),
    path('blog/', include('Blog.urls', namespace='blog')),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

