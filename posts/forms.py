
from django import forms #ModelForm, TextInput
from .models import Problem, Comment
from pagedown.widgets import PagedownWidget
from accounts.models import CustomUser as User

class ProposeForm(forms.ModelForm):

	def coordinators(self):
		people = User.objects.all()
		people_names = []
		for person in people:
			if(person.is_staff == True):
				people_names.append((person.username, person.username))
		return people_names

	def __init__(self, *args, **kwargs):
		super(ProposeForm, self).__init__(*args, **kwargs)
		i=0
		placeholders=['Title','Problem Statement, Constraints, Sample input and output. Without story','','','']
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control createFormCustomStyle'
			visible.field.widget.attrs['placeholder'] = placeholders[i]
			print(visible.field)
			i=i+1
		
		COORDINATOR_CHOICES = self.coordinators()
		self.fields.get('coordinator1').choices = COORDINATOR_CHOICES
		self.fields.get('coordinator2').choices = COORDINATOR_CHOICES	

	Description = forms.CharField(widget=PagedownWidget())
	coordinator1=forms.ChoiceField(choices=[])
	coordinator2=forms.ChoiceField(choices=[])
	class Meta:
		model = Problem
		fields = ['title', 'Description', 'difficulty', 'coordinator1', 'coordinator2']
		fields_required = ['title', 'Description']

class EditForm(forms.ModelForm):
	Description = forms.CharField(widget=PagedownWidget())
	coordinator1=forms.ChoiceField(choices=[])
	coordinator2=forms.ChoiceField(choices=[])
	def coordinators(self):
		people = User.objects.all()
		people_names = []
		for person in people:
			if(person.is_staff == True):
				people_names.append((person.username, person.username))
		return people_names
	def __init__(self, *args, **kwargs):
		super(EditForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control createFormCustomStyle'
		
		COORDINATOR_CHOICES = self.coordinators()
		self.fields.get('coordinator1').choices = COORDINATOR_CHOICES
		self.fields.get('coordinator2').choices = COORDINATOR_CHOICES	
			
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