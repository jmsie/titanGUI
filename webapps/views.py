from django.shortcuts import render

# Create your views here.

def dash_board(request):
  return render(request, 'dash_board.html')

def new_population(request):
  return render(request, 'new_population.html')

def manage_populations(request):
  return render(request, 'manage_population.html')

def add_instrument(request):
  return render(request, 'add_instrument.html')

def manage_instrument(request):
  return render(request, 'manage_instrument.html')

def simulation_result(request):
  return render(request, 'simulation_result.html')
