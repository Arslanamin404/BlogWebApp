from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'author', 'uploaded_at')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'message', 'uploaded_at')


@admin.register(Comment)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'email', 'content', 'publish')
