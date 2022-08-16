from django.shortcuts import render
from .models import DesignInfo
from django.http.response import Http404

def library(request):
    designs = DesignInfo.objects.all()    
    return render(request, "library.html", {'designs':designs})

def individual(request):
    return render(request, "individual.html", {})
