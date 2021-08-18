from django.contrib import admin
from django import forms
# Register your models here.

from .models import Problem, Comment
from pagedown.widgets import AdminPagedownWidget
from django.db import models

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title' , 'author', 'created', 'status')
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }
    fields = ['title', 'author', 'Description','difficulty', 'status']
    inlines = [
        CommentInline,
    ]


admin.site.register(Problem, AuthorAdmin)
admin.site.register(Comment)
