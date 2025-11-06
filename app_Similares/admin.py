from django.contrib import admin
from .models import Cliente, Medicamento, Venta

# Registra tus modelos aquí.
admin.site.register(Cliente)
admin.site.register(Medicamento) # Se registra, pero el enfoque principal es en Cliente por ahora
admin.site.register(Venta)       # Se registra, pero el enfoque principal es en Cliente por ahora