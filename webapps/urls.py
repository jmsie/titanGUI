from django.urls import path, re_path                                                                                                                                      
from django.conf.urls import url 
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [ 
  path("", views.dash_board, name="dash_board"),
  path("new_population", views.new_population, name="new_population"),
  path("manage_population", views.manage_populations, name="manage_population"),
  path("add_instrument", views.add_instrument, name="add_instrument"),
  path("manage_instrument", views.manage_instrument, name="manage_instrument"),
  path("simulation_result", views.simulation_result, name="simulation_result"),
]

