from django.contrib import admin

from Blog.models import BlogModel, CategoryModel
# Register your models here.


@admin.register(BlogModel)
class BlogModelAdmin(admin.ModelAdmin):
	list_display = ['title', 'created']


admin.site.register(CategoryModel)
