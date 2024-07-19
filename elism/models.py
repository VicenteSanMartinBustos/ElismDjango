from django.db import models
from django.conf import settings
# Create your models here.


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=3)
    imagen = models.ImageField(upload_to='products/', default='products/default.png')

    def __str__(self):
        return self.nombre

    
# models.py
# models.py

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    correo_electronico = models.EmailField()
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre


class Carrito(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        self.subtotal = self.cantidad * self.producto.precio
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.usuario.username} - {self.producto.nombre}"


