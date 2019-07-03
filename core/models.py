from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class MyUserManager(BaseUserManager):
    def create_user(self,email,password_decrypt=None,nombres=None,apellidos=None,address=None,tarjeta=None,password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=MyUserManager.normalize_email(email),
            password_decrypt=password_decrypt,
            nombres=nombres,
            apellidos=apellidos,
            address=address,
            tarjeta=tarjeta,



        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        u = self.create_user(email,
                        
                        
                        password=password,
                        
                    )
        u.is_admin = True
        u.save(using=self._db)
        return u

class MyUser(AbstractBaseUser):
    
    email = models.EmailField(
                        verbose_name='email',
                        max_length=255,
                        unique=True,
                    )
    password_decrypt= models.CharField(max_length=200 , verbose_name="Contraseña",blank=True,null=True,default="")

    nombres= models.CharField(max_length=200 , verbose_name="Nombres",blank=True,null=True,default="")
    apellidos= models.CharField(max_length=200 , verbose_name="Apellidos",blank=True,null=True,default="")
    address=models.CharField(max_length=200,verbose_name="direccion",blank=True,null=True,default="")
    tarjeta=models.CharField(max_length=200,verbose_name="tarjeta",blank=True,null=True,default="")

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

# Create your models here.


class Plato(models.Model):
    nombre= models.CharField(max_length=200 , verbose_name="Plato")
    descripcion= models.TextField(verbose_name="Descripcion")
    image=models.ImageField(default='',verbose_name="Foto",upload_to="productos")
    precio= models.FloatField(verbose_name="Precio")
    stock= models.PositiveIntegerField(verbose_name="Stock")
    created= models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
    updated= models.DateTimeField(auto_now=True,verbose_name="Fecha de ultima modificacion")

    class Meta:
        verbose_name="plato"
        verbose_name_plural="platos"
        ordering=["-created"]

    def __str__(self):
        return self.nombre

class Bebida(models.Model):
    nombre= models.CharField(max_length=200 ,verbose_name="Bebida")
    descripcion= models.TextField(verbose_name="Descripcion")
    image=models.ImageField(default='',verbose_name="Foto",upload_to="productos")
    precio= models.FloatField(verbose_name="Precio")
    stock= models.PositiveIntegerField(verbose_name="Stock")
    created= models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
    updated= models.DateTimeField(auto_now=True,verbose_name="Fecha de ultima modificacion")


    class Meta:
        verbose_name="bebida"
        verbose_name_plural="bebidas"
        ordering=["-created"]

    def __str__(self):
        return self.nombre

class Entrada(models.Model):
    nombre= models.CharField(max_length=200 ,verbose_name="Entrada")
    descripcion= models.TextField(verbose_name="Descripcion")
    image=models.ImageField(default='',verbose_name="Foto",upload_to="productos")
    precio= models.FloatField(verbose_name="Precio")
    stock= models.PositiveIntegerField(verbose_name="Stock")
    created= models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
    updated= models.DateTimeField(auto_now=True,verbose_name="Fecha de ultima modificacion")


    class Meta:
        verbose_name="entrada"
        verbose_name_plural="entradas"
        ordering=["-created"]

    def __str__(self):
        return self.nombre

class Promocion(models.Model):
    nombre= models.CharField(max_length=200 ,verbose_name="Promocion")
    descripcion= models.TextField(verbose_name="Descripcion")
    image=models.ImageField(default='',verbose_name="Foto",upload_to="productos")
    precio= models.FloatField(verbose_name="Precio")
    stock= models.PositiveIntegerField(verbose_name="Stock")
    created= models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
    updated= models.DateTimeField(auto_now=True,verbose_name="Fecha de ultima modificacion")


    class Meta:
        verbose_name="promocion"
        verbose_name_plural="promociones"
        ordering=["-created"]

    def __str__(self):
        return self.nombre

class Carrito(models.Model):
    nombre= models.CharField(max_length=200 ,verbose_name="Carrito")
    descripcion= models.TextField(verbose_name="Descripcion")
    image=models.ImageField(default='',verbose_name="Foto",upload_to="productos")
    precio= models.FloatField(verbose_name="Precio")
    cantidad= models.PositiveIntegerField(verbose_name="Cantidad")
    subtotal=models.FloatField(verbose_name="Subtotal" ,default=None)
    created= models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
    updated= models.DateTimeField(auto_now=True,verbose_name="Fecha de ultima modificacion")



    class Meta:
        verbose_name="carrito"
        verbose_name_plural="carritos"
        ordering=["-created"]

    def __str__(self):
        return self.nombre