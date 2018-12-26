from django.urls import path, re_path                                                                                                                                      
from django.conf.urls import url 
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [ 
  path("dash_board", views.dash_board, name="dash_board"),
  path("new_project", views.new_project, name="new_project"),
  path("manage_project", views.manage_projects, name="manage_project"),
  path("add_instrument", views.add_instrument, name="add_instrument"),
  path("manage_instrument", views.manage_instrument, name="manage_instrument"),
  path("simulation_result", views.simulation_result, name="simulation_result"),
]

