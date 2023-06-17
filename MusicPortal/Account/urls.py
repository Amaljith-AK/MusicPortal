from django.urls import path
from .views import *


urlpatterns = [
    path('signup/',SignupView.as_view(),name='signupview'),
    path('logout/',LogoutView.as_view(),name='lgoutview'),
]