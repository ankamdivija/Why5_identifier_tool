from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('login/', views.login,name="login"),
    path('landingpage/',views.landingpage,name="landingpage"),
    path('signup/', views.signup),
    path('logout/', views.logout),
]