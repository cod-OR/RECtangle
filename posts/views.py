from django.shortcuts import render
import requests
from .forms import (ProposeForm, CommentForm, EditForm)
from django.views.generic import (ListView, FormView, DetailView, DeleteView, CreateView, UpdateView)
from django.views.generic.edit import FormMixin
from .models import Problem, Comment
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
# from accounts.models import CustomUser as User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class IsAllowed(LoginRequiredMixin, UserPassesTestMixin):
	def test_func(self):
		return True
		return self.request.user.staff					  #admins can change staff status of any user to revoke his/her access to the site

class HomePageView(IsAllowed, ListView):
	model =Problem
	template_name = 'home.html'
	context_object_name = 'all_prob_list'				# home page shows a list of all current problems

class CreateProbView(IsAllowed, CreateView):
	model = Problem
	template_name = 'problem_create.html'
	form_class=ProposeForm
	
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super(CreateProbView, self).form_valid(form)


class EditProbView(IsAllowed, UpdateView):
	model = Problem
	template_name = 'problem_edit.html'
	form_class=EditForm							# Edit form has a new field of status, to change status of the problem


class ProbDetailView(IsAllowed, FormMixin , DetailView):
	model = Problem
	template_name = 'problem_detail.html'
	form_class =  CommentForm
	def get_context_data(self, **kwargs):
		context = super(ProbDetailView, self).get_context_data(**kwargs)
		context['form'] = self.get_form()
		context['comments'] = Comment.objects.filter(problem = Problem.objects.get(pk=self.object.pk))
		return context

	def get_success_url(self):
		return reverse_lazy('problem_detail', kwargs={'pk': self.object.pk})

	def post(self, request, *args, **kwargs):
		self.object = self.get_object()
		form = self.get_form()
		if form.is_valid():
			problem = Problem.objects.get(pk=self.object.pk)
			new_comment = form.save(commit=False)
			new_comment.problem = problem 						# every comment is associated with a user and a problem
			new_comment.author = request.user
			new_comment.save()
			return self.form_valid(form)
		else:
			return self.form_invalid(form)

	def form_valid(self, form):
		return super(ProbDetailView, self).form_valid(form)


class DeleteProbView(IsAllowed, DeleteView):
	model = Problem
	template_name = 'problem_delete.html'
	success_url = reverse_lazy('home')			# goes to home page after deleting