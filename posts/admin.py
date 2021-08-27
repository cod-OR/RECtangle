from django.contrib import admin
from django import forms
# Register your models here.

from .models import Problem, Comment
from pagedown.widgets import AdminPagedownWidget
from django.db import models

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    #extra comment rows are omited

class ProblemAdmin(admin.ModelAdmin):
    list_display = ('title' , 'author', 'created', 'status')

    # inside admin panel, all text fields will have markdown support
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }
    fields = ['title', 'author', 'Description','difficulty', 'coordinator1', 'coordinator2', 'status']
    inlines = [
        CommentInline,
    ]


admin.site.register(Problem, ProblemAdmin)
admin.site.register(Comment)
