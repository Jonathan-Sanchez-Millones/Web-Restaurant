from django.contrib import admin
from .models import Plato,Bebida,Promocion,Entrada
from django.contrib.auth import get_user_model

# Register your models here.

User=get_user_model()


class PlatoAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('nombre','precio','stock')
    search_fields=('nombre',)
    list_filter=('created','updated')
  

class BebidaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('nombre','precio','stock')
    search_fields=('nombre',)
    list_filter=('created','updated')
   

class PromocionAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('nombre','precio','stock')
    search_fields=('nombre',)
    list_filter=('created','updated')
   

class EntradaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('nombre','precio','stock')
    search_fields=('nombre',)
    list_filter=('created','updated')
    
class UserAdmin(admin.ModelAdmin):
    search_fields=['email']
    list_display=('nombres','email')

    class Meta:
        model=User
admin.site.register(User,UserAdmin)
admin.site.register(Plato,PlatoAdmin)
admin.site.register(Bebida,BebidaAdmin)
admin.site.register(Promocion,PromocionAdmin)
admin.site.register(Entrada,EntradaAdmin)

