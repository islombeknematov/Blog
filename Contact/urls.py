from django.urls import path
from Contact.views import ContactCreateView

app_name = 'contact'

urlpatterns = [
    path('', ContactCreateView.as_view(), name='contact_create'),
#   path('', contact_create, name='contact_create'),
]





