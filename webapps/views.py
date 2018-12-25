from django.shortcuts import render

# Create your views here.

def dash_board(request):
  return render(request, 'dash_board.html')

def new_project(request):
  return render(request, 'new_project.html')
