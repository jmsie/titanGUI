from django.shortcuts import render
from webapps.models import *

# Create your views here.

def dash_board(request):
  return render(request, 'dash_board.html')

def new_population(request):
  instruments = Instrument.objects.all()
  simulation_setting_files = Simulation_setting_file.objects.all()
  seq_defs = Seq_def.objects.all()
  signal_def_files = Signal_def_file.objects.all()
  resolutions = Resolution.objects.all()

  context = {
    "instruments": instruments,
    "years": range(1990, 2020),
    "months": range(1, 13),
    "days": range(1, 32),
    "simulation_setting_files": simulation_setting_files,
    "seq_defs": seq_defs,
    "signal_def_files": signal_def_files,
    "resolutions": resolutions,

  }
  return render(request, 'new_population.html', context)

def manage_populations(request):
  return render(request, 'manage_population.html')

def add_instrument(request):
  return render(request, 'add_instrument.html')

def manage_instrument(request):
  return render(request, 'manage_instrument.html')

def simulation_result(request):
  return render(request, 'simulation_result.html')
