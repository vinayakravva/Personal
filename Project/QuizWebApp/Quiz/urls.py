from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns=[
    path('',home,name="home"),
    path('register/',register,name='register'),
    path('login/',loginPage,name='login'),
    path('logout/',logoutUser,name='logout'),
    path('view_score',view_score,name="view_score"),
    path('api/check_score',check_score,name='check_score'),
    path('<id>',take_quiz,name='take_quiz'),
    path('api/<id>',api_question,name='api_question'),
    
]