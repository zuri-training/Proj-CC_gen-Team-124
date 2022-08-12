from django.urls import path
from . import views

urlpatterns = [
    path('how-it-works', views.documentation, name="how-it-works")
]
