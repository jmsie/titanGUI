from django.shortcuts import render
from django.http import JsonResponse
from webapps.models import *
from webapps.helpers import *
import json

def get_signal_defs(request):
  signal_def = Signal_defs()
  return JsonResponse(signal_def.get_signal_defs(request.POST.get('file_name')), safe=False)

def save_signal_defs(request):
  signal_def = Signal_defs()
  if signal_def.save_signal_defs(request):
    return JsonResponse({"status": "success"})
  return JsonResponse({"status": "fail"})


def manage_signal_defs(request):
  signal_defs = Signal_defs()
  context = {
    "files": signal_defs.get_signal_def_files()
  }
  return render(request, "manage_signal_defs.html", context)

def manage_simulation_settings(request):
  simulation_settings = Simulation_settings()
  context = {
    "files": simulation_settings.get_setting_files(),
  }
  return render(request, 'manage_simulation_settings.html', context)

def get_simulation_settings(request):
  simulation_settings = Simulation_settings()
  return JsonResponse(
    simulation_settings.get_simulation_settings(request.POST.get('file_name')))

def save_simulation_settings(request):
  simulation_settings = Simulation_settings()
  if simulation_settings.save_simulation_settings(request):
    return JsonResponse({"status": "success"})
  return JsonResponse({"status": "fail"})

def dash_board(request):
  return render(request, 'dash_board.html')

def console(request):
  return render(request, 'console.html')

def console_send_command(request):
  command = request.POST.get("command")
  response = send_command(command)
  status = "OK"

  context = {
    "status": status,
    "message": response[-1],
  }
  return JsonResponse(context)

def new_population(request):
  signal_def = Signal_defs()
  simulation_settings = Simulation_settings()

  instruments = Instrument.objects.all()
  simulation_setting_files = simulation_settings.get_setting_files()
  seq_defs = Seq_def.objects.all()
  signal_def_files = signal_def.get_signal_def_files()
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
  populations = get_command_json(send_command("_gui_container_list_population"))
  context = {}
  if "list" in populations:
    context = {
      "populations": populations['list']
    }
  else:
    context = {
      "msg": populations['msg']
    }
  return render(request, 'manage_population.html', context)

def add_instrument(request):
  return render(request, 'add_instrument.html')

def manage_instrument(request):
  return render(request, 'manage_instrument.html')

def simulation_result(request, current_population):
  def floar2String(num):
    if num == None:
      return "N/A"
    return "{:.1f}".format(num)

  sequences = get_command_json(send_command("_gui_container_list_sequence"))
  if len(sequences['list']) == 0:
    send_command("set_current_population " + current_population)
    send_command("get_top_sequences -sequence_name gui_L -method_name  base:mix+L -num 3")
    send_command("get_top_sequences -sequence_name gui_S -method_name  base:mix+S -num 3")
    sequences = get_command_json(send_command("_gui_container_list_sequence"))

  sequences_L = []
  sequences_S = []
  for index, sequence_name in enumerate(sequences['list']):
    send_command("prepare_strategy_report -sequence " + sequence_name)
    sequences_report = get_command_json(send_command("_gui_show_sequence  -sequence " + sequence_name))
    mdd = floar2String(sequences_report['dict']['rpt']['mdd'])
    profit = floar2String(sequences_report['dict']['rpt']['profit'])

    seq = {
      "index": index,
      "name": sequence_name,
      "MDD": mdd,
      "profit": profit,
    }

    if "L" in sequence_name:
      sequences_L.append(seq)
    else:
      sequences_S.append(seq)


  status = "OK"
  context = {
    "status": status,
    "sequences_L": sequences_L,
    "sequences_S": sequences_S,
    "current_population": current_population,
  }
  print(context)

  return render(request, 'simulation_result.html', context)


### API ###
def create_population_and_add_resolutions(request):

  simulation_setting_file = request.POST.get('simulation_setting_file')
  signal_def_file = request.POST.get('signal_def_file')
  seq_def = request.POST.get('seq_def')
  range = build_time_range(request)
  instrument = request.POST.get('instrument')
  population_name = request.POST.get('population_name')
  resolutions = request.POST.get('resolutions')

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
  if population_name is None:
    errors.append('No population name found')
  if resolutions is None:
    errors.append("No resolutions found")

  if len(errors) != 0:
    return JsonResponse({"errors": errors})



  # Build query
  create_population = 'create_population -settings #simulation_setting_file -signal_def #signal_def_file -range #range -instrument #instrument -seqdef #seq_def #population_name -strategy #strategy'
  data = {
    "#simulation_setting_file": simulation_setting_file,
    "#signal_def_file": signal_def_file,
    "#range": range,
    "#instrument": instrument,
    "#seq_def": seq_def,
    "#strategy": 'mc',
    "#population_name": population_name,
  }

  for key, value in data.items():
    create_population = create_population.replace(key, value)



  # Save query to db
  population_obj = Population()
  population_obj.name = population_name
  population_obj.instrument = Instrument.objects.get(name=instrument)
  population_obj.seq_def = Seq_def.objects.get(name=seq_def)
  population_obj.signal_def_file = ""
  population_obj.simulation_setting_file = ""
  population_obj.start_date = range.split('-')[0]
  population_obj.end_date = range.split('-')[1]
  population_obj.resolutions = resolutions[:-1]
  population_obj.query = create_population
  population_obj.save()

  add_resolution = "add_resolution " + population_name + " " + resolutions.replace(',',' ')

  context = {
    "create_population": create_population,
    "add_resolution": add_resolution,
  }

  send_command(create_population)
  send_command(add_resolution)

  return JsonResponse(context)




def cg_write(request):
  seq_name = request.POST.get('seq_name')
  path = "./saves/codes/"+seq_name+".txt"
  send_command("cg_write -sequence "+seq_name+" -file " + path)
  context = {
    "path": path,
    "file_name": seq_name+".txt",
  }
  return JsonResponse(context)












