from django.urls import path
from . import views

urlpatterns = [
    path('our-team', views.team, name="our-team")
]
