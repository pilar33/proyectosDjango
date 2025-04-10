from django.urls import path
from app import views

urlpatterns = [
    # mapeamos la vista creada
    path("", views.Inicio, name="inicio"),
    path("contacto/", views.Contacto,name="contacto")
]