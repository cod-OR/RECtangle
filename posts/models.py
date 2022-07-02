from django.conf import settings
from django.db import models
from django.urls import reverse
from accounts.models import CustomUser as User

class Problem(models.Model):

	def coordinators():
		people = User.objects.all()
		people_names = []
		for person in people:
			people_names.append((person.username, person.username))
		return people_names

	DIFFICULTY_CHOICES = [('A','A'), ('B','B'), ('C','C'), ('D','D'), ('E','E'), ('F','F'), ('G','G'), ('H','H')]
	STATUS_CHOICES = [('Queued','Queued'),('Rejected','Rejected'), ('Accepted','Accepted'), ('Uploaded','Uploaded')]

	COORDINATOR_CHOICES = coordinators()

	title = models.CharField(max_length = 200, null = True, unique =True )
	Description = models.TextField()
	author = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		related_name ='problem_author',
		on_delete=models.CASCADE,
		null = True,
	)

	difficulty = models.CharField(max_length = 30,
								  choices=DIFFICULTY_CHOICES,
								  default='A')
	status = models.CharField(max_length = 30,
								  choices=STATUS_CHOICES,
								  default='Queued')

	created = models.DateTimeField(auto_now_add=True , blank = True, null = True)
	updated = models.DateTimeField(auto_now=True , blank = True, null = True)


	coordinator1 = models.CharField(max_length = 20,
								  choices=COORDINATOR_CHOICES,
								  default='A')
	coordinator2 = models.CharField(max_length = 20,
								  choices=COORDINATOR_CHOICES,
								  default='A')

	class Meta:
		ordering = ('difficulty',)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('problem_detail', args=[str(self.id)])



class Comment(models.Model):
	problem = models.ForeignKey(Problem, related_name ='comments',
							   on_delete = models.CASCADE)
	author = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		related_name ='comment_author',
		on_delete=models.CASCADE,
		null = True,
	)
	comment = models.TextField()
	created = models.DateTimeField(auto_now_add = True, blank=True, null = True)

	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return 'Comment by {} on {}'.format(self.author, self.problem)

	def get_success_url(self):
		print("Inside model!")
		return reverse_lazy('problem_detail', kwargs={'pk': self.object.pk})
