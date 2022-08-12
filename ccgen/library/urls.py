from django.urls import path
from . import views

urlpatterns = [
    path('library', views.library, name="library"),
    path('library/individual-card', views.individual, name="individual-card")
]