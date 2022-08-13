from django.shortcuts import render
from .models import DesignInfo

def library(request):
    designs = DesignInfo.objects.all()    
    return render(request, "library.html", {'designs':designs})

def individual(request):
    return render(request, "individual.html")
