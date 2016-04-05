from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Post, Tag

# Register your models here.

admin.site.register(Post, MarkdownxModelAdmin)
admin.site.register(Tag)
