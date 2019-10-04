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
  path('manage_simulation_settings', views.manage_simulation_settings, name="manage_simulation_settings"),
  path('manage_signal_defs', views.manage_signal_defs, name="manage_signal_defs"),

  path('api/create_population_and_add_resolutions', views.create_population_and_add_resolutions, name="create_population_and_add_resolutions"),
  path('api/console', views.console_send_command, name="console_send_command"),
  path('api/cg_write', views.cg_write, name="cg_write"),
  path('api/get_simulation_settings', views.get_simulation_settings, name="get_simulation_settings"),
  path('api/save_simulation_settings', views.save_simulation_settings, name="save_simulation_settings"),
  path('api/get_signal_defs', views.get_signal_defs, name="get_signal_defs"),
  path('api/save_signal_defs', views.save_signal_defs, name="save_signal_defs"),

]

