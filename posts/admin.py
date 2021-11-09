from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status',)
    search_filed = ('title', 'content')
    prepopulated_fileds = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
