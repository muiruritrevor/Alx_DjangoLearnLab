from django.contrib import admin
from .models import Post

class postadmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')
    list_filter = ('published_date', 'title')
    search_fields = ['title', 'content']
    

admin.site.register(Post)

# Register your models here.
