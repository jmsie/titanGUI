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
  path("simulation_result/<str:current_population>", views.simulation_result, name="simulation_result"),
  path('console', views.console, name="console"),

  path('api/create_population_and_add_resolutions', views.create_population_and_add_resolutions, name="create_population_and_add_resolutions"),
  path('api/console', views.console_send_command, name="console_send_command"),
  path('api/cg_write', views.cg_write, name="cg_write")
]

