from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'publish')
	list_filter = ('status', 'created', 'author')
	prepopulated_fields = { 'slug': ('title',) }
	date_hierarchy = 'publish'

admin.site.register(Post, PostAdmin)
