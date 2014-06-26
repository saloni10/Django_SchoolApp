from django.shortcuts import render
from info.models import *
# Create your views here.

def index(request):
	return render(request, 'index.html')


def display(request):
    
    results=[]
    avail_list = ['name','roll_no','branch','session','marks','backlog']
    if 'info' in request.GET:
       info = request.GET.getlist('info')
       for i in avail_list :
          if i in info :
            obj= Student.objects.values(i) 
            results.append(obj)  
             
     
       return render(request, 'display.html', {'info': info, 'results':results })
 
    
    else:
       
       return render(request, 'display.html', {'error': True, 'nothing': nothing})
   





