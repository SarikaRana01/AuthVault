
from django.urls import path,include
from .views import *

urlpatterns = [
   
    path('', signUp, name='signUp'),
    path('login/',login, name='login'),
    path('logout/',logout, name='logout'),
]