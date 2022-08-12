from django.shortcuts import render

def documentation(request):
    return render(request, "how-it-works.html")
