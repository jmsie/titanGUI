from django.shortcuts import render
from django.http import JsonResponse
from webapps.models import *
from webapps.helpers import *

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


### API ###
def create_population(request):

  simulation_setting_file = request.POST.get('simulation_setting_file')
  signal_def_file = request.POST.get('signal_def_file')
  seq_def = request.POST.get('seq_def')
  range = build_time_range(request)
  instrument = request.POST.get('instrument')
  name = request.POST.get('population_name')

  errors = []
  if simulation_setting_file is None:
    errors.append('No simulation files found')
  if signal_def_file is None:
    errors.append('No signal def found')
  if seq_def is None:
    errors.append('No sew def found')
  if range is None:
    errors.append('Time range setting error')
  if instrument is None:
    errors.append('No instrument found')
  if name is None:
    errors.append('No population name found')

  if len(errors) != 0:
    return JsonResponse({"errors": errors})



  # Build query
  query_template = 'create_population -settings #simulation_setting_file -signal_def #signal_def_file -range #range -instrument #instrument -seqdef #seq_def #name'
  data = {
    "#simulation_setting_file": simulation_setting_file,
    "#signal_def_file": signal_def_file,
    "#range": range,
    "#instrument": instrument,
    "#seq_def": seq_def,
    "#name": name,
  }

  for key, value in data.items():
    query_template = query_template.replace(key, value)

  context = {
    "query": query_template,
  }

  # Save query to db
  population_obj = Population()
  population_obj.name = name
  population_obj.instrument = Instrument.objects.get(name=instrument)
  population_obj.seq_def = Seq_def.objects.get(name=seq_def)
  population_obj.signal_def_file = Signal_def_file.objects.get(name=signal_def_file)
  population_obj.simulation_setting_file = Simulation_setting_file.objects.get(name=simulation_setting_file)
  population_obj.start_date = range.split('-')[0]
  population_obj.end_date = range.split('-')[1]
  population_obj.query = query_template
  population_obj.save()



  return JsonResponse(context)




