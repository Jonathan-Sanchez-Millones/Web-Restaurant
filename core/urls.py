from django.urls import path
from . import views

urlpatterns = [
   
    path('',views.home,name="home"),
    path('platos/',views.platos,name="platos"),
    path('entradas/',views.entradas,name="entradas"),
    path('bebidas/',views.bebidas,name="bebidas"),
    path('promociones/',views.promociones,name="promociones"),
    path('carrito/',views.carrito,name="carrito"),
    path('pago/',views.pago,name="pago"),
    path('addcarrito/',views.addcarrito,name="addcarrito"),
    path('addcarritoentrada/',views.addcarritoentrada,name="addcarritoentrada"),
    path('addcarritoplato/',views.addcarritoplato,name="addcarritoplato"),
    path('addcarritobebida/',views.addcarritobebida,name="addcarritobebida"),
    path('deleteproducto/',views.deleteproducto,name="deleteproducto"),
    path('register/',views.createUser,name="register"),
    path('login/',views.login,name="login"),
    path('updatecarrito/',views.updatecarrito,name="updatecarrito"),
    path('deletecarrito/',views.deletecarrito,name="deletecarrito"),



    ]