
from django import forms #ModelForm, TextInput
from .models import Problem, Comment
from pagedown.widgets import PagedownWidget

class ProposeForm(forms.ModelForm):
	Description = forms.CharField(widget=PagedownWidget())
	class Meta:
		model = Problem
		fields = ['title', 'Description', 'difficulty']
		fields_required = ['title', 'Description']

class EditForm(forms.ModelForm):
	Description = forms.CharField(widget=PagedownWidget())
	class Meta:
		model = Problem
		fields = ['title', 'Description', 'difficulty', 'status']
		fields_required = ['title', 'Description']


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['comment']
		fields_required = ['comment']		