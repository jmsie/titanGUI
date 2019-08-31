import datetime
from django.conf import settings
import json

def build_time_range(request):
  start_year = request.POST.get('start_year')
  start_month = request.POST.get('start_month')
  start_day = request.POST.get('start_day')

  end_year = request.POST.get('end_year')
  end_month = request.POST.get('end_month')
  end_day = request.POST.get('end_day')

  # Format and validate numbers
  start_year = format_number(start_year)
  start_month = format_number(start_month)
  start_day = format_number(start_day)
  end_year = format_number(end_year)
  end_month = format_number(end_month)
  end_day = format_number(end_day)

  if start_year is None or start_month is None or start_day is None:
    return None
  if end_year is None or end_month is None or end_day is None:
    return None

  start_time = get_time_stamp(start_year + '-' + start_month + '-' + end_day)
  end_time = get_time_stamp(end_year + '-' + end_month + '-' + end_day)
  if end_time < start_time:
    return None

  return start_year+"_"+start_month+start_day+"-"+end_year+"_"+end_month+end_day


def format_number(str):
  if not is_int(str):
    return None

  if int(str) < 10:
    return '0' + str
  else:
    return str


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
def send_command(command):
  import sys
  sys.path.append(settings.TITAN)
  import logging
  from titan.ui_titan import TitanSocketUi
  from cmdshell.log import SocketHandler
  import socket
  # Communicate with Titan server
  socket_handler = SocketHandler()
  recv = []
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    socket_handler.set_socket(sock)
    try:
      sock.connect((settings.TITAN_HOST, settings.TITAN_PORT))
      TitanSocketUi.send_str(sock, command)
      for data in socket_handler.receive():
        recv.append(data.getMessage())
    except ConnectionRefusedError:
      msg = "Cannot connect to the server at {}:{}".format(
        settings.TITAN_HOST, settings.TITAN_PORT)
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
