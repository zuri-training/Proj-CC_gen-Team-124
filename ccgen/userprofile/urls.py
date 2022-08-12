from django.urls import path
from . import views

urlpatterns = [
    path('profile', views.profile, name="profile"),
    path('saved-designs', views.saved_designs, name="saved-designs")
]