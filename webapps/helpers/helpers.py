import datetime
from django.conf import settings
import json

class Signal_defs():
  def __init__(self):
    self.path = settings.TITAN + "/signal_defs/"
    self.posfix = ".signal_def.yml"

  def get_signal_def_files(self):
    from os import listdir
    files = []
    for file in listdir(self.path):
      files.append(file.split('.')[0])
    return files

  def get_signal_defs(self, file_name):
    import yaml, json
    data = ""
    file = self.path + file_name + self.posfix
    with open(file) as fp:
      data = yaml.load(fp, Loader=yaml.FullLoader)
    return json.dumps(data, indent=2)

  def save_signal_defs(self, request):
    import yaml, json
    file_name = request.POST.get('file_name')
    file = self.path + file_name + self.posfix
    signal_def_json = json.loads(request.POST.get('signal_defs'))

    with open(file, "w") as fp:
      yaml.dump(signal_def_json, fp)
    fp.close()

class Simulation_settings():
  def __init__(self):
    self.path = settings.TITAN + "/settings/"
    self.posfix = ".setting.yml"

  def get_setting_files(self):
    from os import listdir
    files = []
    for file in listdir(self.path):
      files.append(file.split('.')[0])
    return files

  def get_simulation_settings(self, file_name):
    settings = {}
    file = self.path + file_name + self.posfix
    with open(file) as fp:
      while True:
        line = fp.readline()
        if line:
          if line[0] == "#" or len(line) == 0:
            continue
          name, parameter = line[:-1].split(':')
          settings[name] = parameter
        else:
          break
    return settings

  def save_simulation_settings(self, request):
    file_name = request.POST.get('file_name')
    file = self.path + file_name + self.posfix
    with open(file, "w") as fp:
      for key, value in request.POST.items():
        if key == "file_name" or key == "csrfmiddlewaretoken":
          continue
        else:
          fp.write("{}: {}\n".format(key, value))
    fp.close()


def build_out_sample_time_range(request, end_date):
  from datetime import date
  try:
    start_year = int(request.POST.get('end_year'))
    start_month = int(request.POST.get('end_month'))
    start_day = int(request.POST.get('end_day'))

    start_date = date(start_year, start_month, start_day)
    return build_time_range(start_date, end_date)
  except:
    return None

def build_in_sample_time_range(request):
  from datetime import date
  start_year = int(request.POST.get('start_year'))
  start_month = int(request.POST.get('start_month'))
  start_day = int(request.POST.get('start_day'))

  end_year = int(request.POST.get('end_year'))
  end_month = int(request.POST.get('end_month'))
  end_day = int(request.POST.get('end_day'))

  start_date = date(start_year, start_month, start_day)
  end_date = date(end_year, end_month, end_day)
  return build_time_range(start_date, end_date)

def build_time_range(start_date, end_date):
  # Format and validate numbers
  start_year = format_number(start_date.year)
  start_month = format_number(start_date.month)
  start_day = format_number(start_date.day)
  end_year = format_number(end_date.year)
  end_month = format_number(end_date.month)
  end_day = format_number(end_date.day)

  start_time = get_time_stamp(start_year + '-' + start_month + '-' + end_day)
  end_time = get_time_stamp(end_year + '-' + end_month + '-' + end_day)
  if end_time < start_time:
    return None

  return start_year+"_"+start_month+start_day+"-"+end_year+"_"+end_month+end_day


def format_number(num):
  if num < 10:
    return '0' + str(num)
  else:
    return str(num)


def is_int(str):
  for char in str:
    if ord(char) < 48 or ord(char) > 57:
      return False
  return True

def get_time_stamp(str):
  return int(datetime.datetime.strptime(str, '%Y-%m-%d').strftime("%s"))


# This function loads the TitanSocketUi to handle the connection
# between GUI and Titan server.
# @input: string
# @output: string
def send_command(command, out_sample=False):
  try:
    from titan.ui_titan import TitanSocketUi
    from cmdshell.log import SocketHandler
  except:
    import sys
    sys.path.append(settings.TITAN)
    from titan.ui_titan import TitanSocketUi
    from cmdshell.log import SocketHandler
  import socket
  if out_sample:
    HOST = settings.TITAN_HOST_OUT_SAMPLE
    PORT = settings.TITAN_PORT_OUT_SAMPLE
  else:
    HOST = settings.TITAN_HOST
    PORT = settings.TITAN_PORT
  # Communicate with Titan server
  socket_handler = SocketHandler()
  recv = []
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    socket_handler.set_socket(sock)
    try:
      sock.connect((HOST, PORT))
      TitanSocketUi.send_str(sock, command)
      for data in socket_handler.receive():
        recv.append(data.getMessage())
    except ConnectionRefusedError:
      msg = "Cannot connect to the server at {}:{}".format(
        HOST, PORT)
      recv.append(json.dumps({"msg":msg}))

  return recv

# This function defines how to get the json form the titan response
def get_command_json(string):
  print(string)
  return json.loads(string[-1])


def is_json(string):
  try:
    json_object = json.loads(string)
  except ValueError:
    return False
  return True
