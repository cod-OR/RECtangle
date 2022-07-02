
from django import forms #ModelForm, TextInput
from .models import Problem, Comment
from pagedown.widgets import PagedownWidget

class ProposeForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(ProposeForm, self).__init__(*args, **kwargs)
		i=0
		placeholders=['Title','Problem Statement, Constraints, Sample input and output. Without story','','','']
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control createFormCustomStyle'
			visible.field.widget.attrs['placeholder'] = placeholders[i]
			i=i+1

	Description = forms.CharField(widget=PagedownWidget())
	class Meta:
		model = Problem
		fields = ['title', 'Description', 'difficulty', 'coordinator1', 'coordinator2']
		fields_required = ['title', 'Description']

class EditForm(forms.ModelForm):
	Description = forms.CharField(widget=PagedownWidget())
	def __init__(self, *args, **kwargs):
		super(EditForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control createFormCustomStyle'
			
	class Meta:
		model = Problem
		fields = ['title', 'Description', 'difficulty',  'coordinator1', 'coordinator2', 'status']
		fields_required = ['title', 'Description']


class CommentForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(CommentForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'
			print(visible.label)
			if(visible.label == 'Comment'):
				visible.label = 'Comment Here:'
				visible.field.widget.attrs['rows'] = 3
	class Meta:
		model = Comment
		fields = ['comment']
		fields_required = ['comment']		