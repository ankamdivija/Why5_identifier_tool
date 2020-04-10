from django.urls import path
from . import views

urlpatterns = [
    path('public_dashboard/', views.public_dashboard,name="public_dashboard"),
    path('create_post/', views.create_post,name="create_post"),
    path('private_dashboard/', views.private_dashboard,name="private_dashboard"),
]