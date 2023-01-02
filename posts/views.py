from django.shortcuts import render
import requests
from .forms import (ProposeForm, CommentForm, EditForm)
from django.views.generic import (ListView, FormView, DetailView, DeleteView, CreateView, UpdateView)
from django.views.generic.edit import FormMixin
from .models import Problem, Comment
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
from accounts.models import CustomUser as User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail
from django.conf import settings
# from django.contrib.auth.models import User

class IsAllowed(LoginRequiredMixin, UserPassesTestMixin):
	def test_func(self):
		return self.request.user.is_staff
		#admins can change staff status of any user to revoke his/her access to the site

class UpdateEmailSender():
	def sendEmailToBM(self,bmlist,content):
		subject = "New activity on RECtangle!"
		send_mail(
			subject=subject,
			message=content,
			from_email=settings.EMAIL_HOST_USER,
			recipient_list=bmlist
		)
	# def __init__(bmlist = []):
		# all_users = User.objects.values()
		# for user in all_users:
		# 	if user['post'] == 'BoardMember':
		# 		bmlist.append(user['email'])

class HomePageView(IsAllowed, ListView):
	model =Problem
	template_name = 'home.html'
	context_object_name = 'all_prob_list'
	# home page shows a list of all current problems

class CreateProbView(IsAllowed, CreateView, UpdateEmailSender):
	model = Problem
	template_name = 'problem_create.html'
	form_class=ProposeForm
	def form_valid(self, form):
		form.instance.author = self.request.user
		bmlist =[]
		all_users = User.objects.values()
		for user in all_users:
			if user['post'] == 'BoardMember':
				bmlist.append(user['email'])
		self.sendEmailToBM(bmlist,str(form.instance.author) + "has posted new problem. \nCoordinator: " +str(form.instance.coordinator1) + "\nDifficulty: " + str(form.instance.difficulty))
		return super(CreateProbView, self).form_valid(form)


class EditProbView(IsAllowed, UpdateView, UpdateEmailSender):
	model = Problem
	template_name = 'problem_edit.html'
	form_class=EditForm
	# Edit form has a new field of status, to change status of the problem

	def form_valid(self, form):
		content = str(self.request.user) + " has edited a problem. " + "\nTitle: " + str(form.instance.title) + "\nCoordinator: " +str(form.instance.coordinator1) + "\nDifficulty: " + str(form.instance.difficulty)
		bmlist =[]
		all_users = User.objects.values()
		for user in all_users:
			if user['post'] == 'BoardMember':
				bmlist.append(user['email'])
		self.sendEmailToBM(bmlist,content)
		return super(UpdateView, self).form_valid(form)


class ProbDetailView(IsAllowed, FormMixin , DetailView, UpdateEmailSender):
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

	def sendCommentEmail(self, new_comment, problem):
		title = problem.title
		c_author = new_comment.author.username
		comment = new_comment.comment
		subject='New Comment on your problem!'
		content = 'You have a new Comment on the problem '+title+' by '+c_author + '.\n'+ 'Comment - '+ '\"' +comment + '\".'
		if(new_comment.author.username != problem.author.username):
			send_mail(
				subject=subject,
				message=content,
				from_email=settings.EMAIL_HOST_USER,
				recipient_list=[problem.author.email]
			)


	def post(self, request, *args, **kwargs):
		self.object = self.get_object()
		form = self.get_form()
		bmlist =[]
		all_users = User.objects.values()
		for user in all_users:
			if user['post'] == 'BoardMember':
				bmlist.append(user['email'])
		if form.is_valid():
			problem = Problem.objects.get(pk=self.object.pk)
			new_comment = form.save(commit=False)
			new_comment.problem = problem 						# every comment is associated with a user and a problem
			new_comment.author = request.user
			new_comment.save()
			self.sendEmailToBM(bmlist,str(new_comment.author) + " commented on problem \"" + str(problem.title) +"\"")
			self.sendCommentEmail(new_comment, problem)
			return self.form_valid(form)
		else:
			return self.form_invalid(form)


class DeleteProbView(IsAllowed, DeleteView, UpdateEmailSender):
	model = Problem
	template_name = 'problem_delete.html'
	success_url = reverse_lazy('home')

	# goes to home page after deleting
