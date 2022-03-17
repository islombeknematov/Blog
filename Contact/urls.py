from django.urls import path
from Contact.views import ContactCreateView, ContactModelListAPIView

app_name = 'contact'

urlpatterns = [
    path('', ContactCreateView.as_view(), name='contact_create'),
#   path('', contact_create, name='contact_create'),
    
    path('api/', ContactModelListAPIView.as_view(), name='c_api'),
]





