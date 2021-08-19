from django.contrib import admin
from .models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm

User = get_user_model()

admin.site.unregister(Group)

class UserAdmin(BaseUserAdmin):
	
	form = CustomUserChangeForm
	add_form = CustomUserCreationForm

	# the list shown in admin panel
	list_display = ['username' , 'post' ,'email', 'is_superuser', 'staff']
	
	list_filter = ['is_superuser', 'post']
	fieldsets = (
		(None, {'fields': ('username', 'email', 'password', 'post', 'is_superuser', 'staff')}),
	)
	
	add_fieldsets = (
		(None, {
			'fields': ('username' , 'email', 'password1', 'password2', 'post', 'is_superuser', 'staff')}
		),
	)

	search_fields = ['username']

admin.site.register(CustomUser, UserAdmin)
