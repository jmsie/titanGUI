from django.urls import path, re_path                                                                                                                                      
from django.conf.urls import url 
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [ 
  path("dash_board", views.dash_board, name="dash_board"),
  path("/", views.dash_board, name="dash_board"),
]

