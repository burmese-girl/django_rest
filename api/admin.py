from django.contrib import admin

# Register your models here.
from simple_history.admin import SimpleHistoryAdmin
from . import models

class BlogPostAdmin(SimpleHistoryAdmin):

    list_per_page = 20
    search_fields = ['title']
    ordering = ['title']
    list_display = ['title', 'content', 'public_date']


admin.site.register(models.BlogPost, BlogPostAdmin)