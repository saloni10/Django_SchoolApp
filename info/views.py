from django.shortcuts import render
from info.models import *
# Create your views here.

def index(request):
	return render(request, 'index.html')


def display(request):
 #  error= False
   if 'info' in request.GET:
       info = request.GET.getlist('info')
     #  if not info:
     #      error = True
     #  else:
       return render(request, 'display.html', { 'info': info })
 #  return render(request, 'display.html', {'error':error})
   else:
       a = 'nothing'
       return render(request, 'display.html', {'error': True, 'else':a})
   





