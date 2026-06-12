from django.contrib import admin
from .models import Proyecto
# Register your models here.
# Le decimos a Django que muestre esta tabla en el panel
admin.site.register(Proyecto)