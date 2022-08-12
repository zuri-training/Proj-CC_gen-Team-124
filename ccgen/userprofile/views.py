from django.shortcuts import render

def profile(request):
    return render(request, "profile.html")

def saved_designs(request):
    return render(request, "saved-designs.html")

def edit_profile(request):
    return render(request, "editPage.html")
