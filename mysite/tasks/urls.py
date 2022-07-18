from django.urls import path
from . import views


urlpatterns = [
    # path('helloworld/', views.helloWorld),
    path('', views.taskList, name='task-list'),
    path('task/<int:id>/', views.taskView, name='task-view'),
    path('newtask/', views.newTask, name='task-new'),
    path('yourname/<str:name>', views.yourName, name='your-name'),
    path('edit/<int:id>/', views.editTask, name='task-edit'),
    path('delete/<int:id>/', views.deleteTask, name='task-delete'),
]