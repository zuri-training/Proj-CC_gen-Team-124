from django.urls import path
from . import views
from authentication.forms import UserRegistration

urlpatterns = [
    path('profile', views.profile, name="profile"),
    path('saved-designs', views.saved_designs, name="saved-designs"),
    path('edit', views.edit_profile, name="edit")
]