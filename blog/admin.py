from django.contrib import admin

from blog.models import Category, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'status', 'slug', 'author',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
