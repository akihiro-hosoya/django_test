from django.contrib import admin
from .models import Post, GrandCategory, ParentCategory, Category

admin.site.register(Post)
admin.site.register(GrandCategory)
admin.site.register(ParentCategory)
admin.site.register(Category)
