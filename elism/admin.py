
from django.contrib import admin
from .models import Contacto

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo_electronico', 'mensaje')


from django.contrib import admin
from .models import Producto

admin.site.register(Producto)

