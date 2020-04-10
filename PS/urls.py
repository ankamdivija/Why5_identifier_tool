from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard,name="dashboard"),
    path('create_topic/', views.create_topic, name="create_topic"),
]