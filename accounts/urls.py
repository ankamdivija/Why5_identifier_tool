from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('login/', views.Login,name="login"),
    path('signup/', views.register, name='signup'),
    path('logout/', views.logoutuser, name='logout'),
]