from django.urls import path
from . import views


urlpatterns = [
    path('', views.noticias_jua, name = "noticias_jua"),
]
