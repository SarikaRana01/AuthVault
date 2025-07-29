from django.urls import path
from .views import *

urlpatterns = [
    path("show/",show_dashboard,name="show"),
    path('add/',add_credential, name='add'),
    path('update/<int:pk>/', update_credential, name='update'),
    path('delete/<int:pk>/', delete_credential, name='delete'),
    path("view_password/",view_password,name="view_password")
]

