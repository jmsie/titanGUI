from django.shortcuts import render

# Create your views here.

def dash_board(request):
  return render(request, 'dash_board.html')

def new_project(request):
  return render(request, 'new_project.html')

def manage_projects(request):
  return render(request, 'manage_project.html')

def add_instrument(request):
  return render(request, 'add_instrument.html')

def manage_instrument(request):
  return render(request, 'manage_instrument.html')
