from django.db import models

# Create your models here.

# Convención: en Django se recomienda usar nombres de modelos con la primera letra en mayúscula (Clientes en lugar de clientes), aunque no es obligatorio.
class Clientes(models.Model):
    nombre = models.CharField(max_length=250, blank=True)
    apellido = models.CharField(max_length=150)
    email = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True)

    # si queres personalizar cómo se muestra el objeto, en ese caso debés usar el método __str__
    # Si querés devolver todos los campos formateados en el __str__, podés armar una cadena que combine todo lo que necesitás.
    def __str__(self):
         return f"Nombre: {self.nombre} | Apellido: {self.apellido} | Email: {self.email} | Teléfono: {self.telefono}"
