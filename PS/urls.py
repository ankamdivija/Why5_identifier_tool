from django.urls import path
from . import views

urlpatterns = [

    path('public_dashboard/', views.public_dashboard,name="public_dashboard"),
    path('create_topic/', views.create_topic,name="create_topic"),
    path('private_dashboard/', views.private_dashboard,name="private_dashboard"),

]