from django.contrib import admin

# Register your models here.

from .models import Usuari

class AdminReg(admin.ModelAdmin):
    list_display= ["nom","email","pwd"]
    list_display_links = ["email"]
    list_editable = ["nom"]
    search_fields = ["email","nom"]
    class Meta:
        model = Usuari

admin.site.register(Usuari,AdminReg)
