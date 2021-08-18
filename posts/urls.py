
from django.urls import path
from .views import HomePageView, CreateProbView, ProbDetailView, DeleteProbView, EditProbView

urlpatterns = [
	path('', HomePageView.as_view(), name = 'home'),
	path('create', CreateProbView.as_view(), name = 'problem_create'),
	path('problem/<int:pk>/', ProbDetailView.as_view(), name = 'problem_detail'),
	path('problem/<int:pk>/delete/', DeleteProbView.as_view(), name='problem_delete'),
	path('problem/<int:pk>/edit/', EditProbView.as_view(), name='problem_edit'),
]	