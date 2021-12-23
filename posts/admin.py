from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on', 'sponsored')
    list_filter = ('status', 'sponsored')
    search_field = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

# admin.site.register(Post, PostAdmin)
