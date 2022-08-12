from django.shortcuts import render

def forgot_pass(request):
    return render(request, "forgot-password.html")
