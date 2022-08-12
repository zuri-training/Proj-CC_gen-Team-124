from django.urls import path
from . import views

urlpatterns = [
    path('forgot-password', views.forgot_pass, name="forgot-password")
]