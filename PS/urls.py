from django.urls import path
from . import views

urlpatterns = [

    path('public_dashboard/', views.public_dashboard,name="public_dashboard"),
    path('post/', views.post_ps,name="post_ps"),
    path('add_post/', views.add_post,name="add_post"),
    path('private_dashboard/', views.private_dashboard,name="private_dashboard"),
    path('response/<str:id>/<str:a_id>/',views.response,name="response"),
    path('add/<str:id>/',views.add_answer,name="add_answer"),


]