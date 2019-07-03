from django.shortcuts import render,get_object_or_404,HttpResponse,redirect,reverse,HttpResponseRedirect
from .models import Promocion,Bebida,Plato,Entrada,Carrito,MyUser
from django.views.decorators.csrf import csrf_exempt
from django.db import connections
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.utils import timezone
from .forms import MyUserForm
import json

User=get_user_model()

# Create your views here.

def home(request):
    return render(request,"core/index.html")
def platos(request):
    platos=Plato.objects.all()
    return render(request,"core/platos.html",{'platos':platos})
def entradas(request):
    entradas=Entrada.objects.all()
    return render(request,"core/entradas.html",{'entradas':entradas})
def bebidas(request):
    bebidas=Bebida.objects.all()
    return render(request,"core/bebidas.html",{'bebidas':bebidas})
def promociones(request):
    promociones=Promocion.objects.all()
    return render(request,"core/promociones.html",{'promociones':promociones})
def carrito(request):
    carritos=Carrito.objects.all()
    subtotal=0
    for carrito in carritos:
            subtotal+=carrito.subtotal

    total=subtotal+3.8
    return render(request,"core/carrito.html",{'carritos':carritos,'subtotal':subtotal,'total':total})
def pago(request):
    carritos=Carrito.objects.all()
    subtotal=0
    for carrito in carritos:
            subtotal+=carrito.subtotal

    total=subtotal+3.8
    return render(request,"core/pago.html",{'carritos':carritos,'subtotal':subtotal,'total':total})
@csrf_exempt    
def addcarrito(request):
    if request.method == 'POST':
        nombre_promocion = request.POST.get('nombre')
        cantidad_promocion = request.POST.get('cantidad')
        promocion=get_object_or_404(Promocion,nombre=nombre_promocion)
        carritos=Carrito.objects.all()
        encontro=False
        for carrito in carritos:
            if carrito.nombre==nombre_promocion:
                encontro=True
                break
        if encontro==False:
            subtotal=int(cantidad_promocion)*promocion.precio
            carrito=Carrito(promocion.id,promocion.nombre,promocion.descripcion,promocion.image,promocion.precio,cantidad_promocion
            ,subtotal)
            carrito.save()
    return HttpResponse(nombre_promocion)

@csrf_exempt    
def addcarritoentrada(request):
    if request.method == 'POST':
        nombre_entrada = request.POST.get('nombre')
        cantidad_entrada = request.POST.get('cantidad')
        entrada=get_object_or_404(Entrada,nombre=nombre_entrada)
        carritos=Carrito.objects.all()
        encontro=False
        for carrito in carritos:
            if carrito.nombre==nombre_entrada:
                encontro=True
                break
        if encontro==False:
            subtotal=int(cantidad_entrada)*entrada.precio
            id=entrada.id+10
            carrito=Carrito(id,entrada.nombre,entrada.descripcion,entrada.image,entrada.precio
            ,cantidad_entrada,subtotal)
            carrito.save()
    return HttpResponse(nombre_entrada)

@csrf_exempt    
def addcarritoplato(request):
    if request.method == 'POST':
        nombre_plato = request.POST.get('nombre')
        cantidad_plato = request.POST.get('cantidad')
        plato=get_object_or_404(Plato,nombre=nombre_plato)
        carritos=Carrito.objects.all()
        encontro=False
        for carrito in carritos:
            if carrito.nombre==nombre_plato:
                encontro=True
                break
        if encontro==False:
            subtotal=int(cantidad_plato)*plato.precio
            id=plato.id+20
            carrito=Carrito(id,plato.nombre,plato.descripcion,plato.image,plato.precio
            ,cantidad_plato,subtotal)
            carrito.save()
    return HttpResponse(nombre_plato)

@csrf_exempt    
def addcarritobebida(request):
    if request.method == 'POST':
        nombre_bebida = request.POST.get('nombre')
        cantidad_bebida = request.POST.get('cantidad')
        bebida=get_object_or_404(Bebida,nombre=nombre_bebida)
        carritos=Carrito.objects.all()
        encontro=False
        for carrito in carritos:
            if carrito.nombre==nombre_bebida:
                encontro=True
                break
        if encontro==False:
            subtotal=int(cantidad_bebida)*bebida.precio
            id=bebida.id+30
            carrito=Carrito(id,bebida.nombre,bebida.descripcion,bebida.image,bebida.precio
            ,cantidad_bebida,subtotal)
            carrito.save()
    return HttpResponse(nombre_bebida)

@csrf_exempt
def deleteproducto(request):
    if request.method == 'POST':
        request_getdata = request.POST.get('nombre')

        carritos=Carrito.objects.all()

        for carrito in carritos:

            if carrito.nombre==request_getdata:
                
                c = connections['default'].cursor()
                c.execute("DELETE FROM CORE_CARRITO WHERE NOMBRE=%s;",[request_getdata])
                break

    return HttpResponse(request_getdata)

def register(request):
    form=UserCreationForm()
    return render(request,"core/register.html")

@csrf_exempt
def createUser(request):
   
    if request.method == 'POST':
        nombres = request.POST.get('nombres')
        apellidos = request.POST.get('apellidos')
        email = request.POST.get('email')
        password = request.POST.get('password')
        direccion = request.POST.get('direccion')
        hour = timezone.now()
        day  = timezone.now()
        print("PASSWORD R:"+password)
        
        myuser=User(password,day,hour,email,password,nombres,apellidos,direccion)
        
        myuser.set_password(password)
        myuser.save()
     
    json = "Te tengo"
    return HttpResponse(json) 
@csrf_exempt
def login(request):
    if request.method == 'POST':
        users=User.objects.all()
        email = request.POST.get('email')
        password = request.POST.get('password')
        response="no existe"
        for user in users:
            
            if user.email==email and user.password_decrypt==password:
                response="existe"+"-"+user.nombres+"-"+user.apellidos
                break
        return HttpResponse(response)

@csrf_exempt
def updatecarrito(request):
    
    data = request.body.decode ('utf-8')
    ourid = json.loads (data)
    productos=ourid.get('productos')
    print("Gaaaaaa:")
    print(ourid)
    print(productos)
    for producto in productos:
        nombre_producto=producto.get('nombre')
        cantidad_nueva=producto.get('cantidad')
        c = connections['default'].cursor()
        c.execute("UPDATE core_carrito  SET cantidad=%s where nombre=%s;",[cantidad_nueva,nombre_producto])
        c.execute("UPDATE core_carrito  SET subtotal=precio*cantidad where nombre=%s;",[nombre_producto])
        
        

    return HttpResponse(data)

@csrf_exempt
def deletecarrito(request):
    
    if request.method == 'POST':

        c = connections['default'].cursor()
        c.execute(" DELETE FROM core_carrito;")
        return HttpResponse("exitooooo")



    

            
