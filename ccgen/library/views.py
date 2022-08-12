from django.shortcuts import render

def library(request):
    return render(request, "library.html")

def individual(request):
    return render(request, "individual.html")
