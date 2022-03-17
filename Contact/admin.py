from django.contrib import admin

# Register your models here.
from Contact.models import ContactModel


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    list_filter = ['created']






