from django.contrib import admin
from .models import Comment, Category, Post, Tag


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'parent', 'name', 'email', 'website', 'message')
    search_fields = ('name', 'email')
    list_filter = ('post',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'title', 'description', 'content',)
    search_fields = ('title', 'category__title', 'tag__title')
    list_filter = ('title',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Tag)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
