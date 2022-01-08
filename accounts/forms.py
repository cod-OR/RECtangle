
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser
from django.contrib.auth import get_user_model
User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
	email = forms.EmailField(required=True)
	class Meta(UserCreationForm):
		model = CustomUser
		fields = UserCreationForm.Meta.fields + ('email', )
		# we require email for password reset!

class CustomUserChangeForm(UserChangeForm):
	class Meta:
		model = CustomUser
		fields = UserChangeForm.Meta.fields
