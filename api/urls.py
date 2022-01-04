from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('list/', views.taskList, name="task-list"),
	path('create/', views.taskCreate, name="task-create"),

]
