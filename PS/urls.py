from django.urls import path
from django.conf.urls import url
from . import views
from accounts.models import UserDetail

urlpatterns = [

    path('public_dashboard/', views.public_dashboard,name="public_dashboard"),
    path('post/', views.create_post,name="create_post"),
    path('private_dashboard/', views.private_dashboard,name="private_dashboard"),
    path('response/<str:id>/<str:a_id>/',views.response,name="response"),
    path('add/<str:id>/',views.add_answer,name="add_answer"),
    path('add/<str:id>/<str:a_id>/',views.add_sub_answer,name="add_sub_answer"),
    path('root/<str:id>/<str:a_id>/',views.root_achieved,name="root_achieved"),
    path('public_dashboard/category=<str:name>',views.category_filter,name="category_filter"),
    path('public_dashboard/tag=<str:name>',views.tag_filter,name="tag_filter"),

]