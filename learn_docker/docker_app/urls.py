from django.urls import path
from docker_app import views

urlpatterns = [
    path('',views.simple_view),
]