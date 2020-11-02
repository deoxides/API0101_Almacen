from django.db import models

# Create your models here.
class TiposProducto(models.TextChoices):
    DEFAULT = u'O', 'OTROS'
    ALIMENTOS = u'A','ALIMENTOS PERECEDEROS Y NO PERECEDEROS'
    BEBIDAS = u'B', 'BEBIDAS'
    ARTICULOS = u'AA', 'ARTICULOS DE ASEO'
    BAZAR = u'PB', 'PRODUCTOS DE BAZAR'

class Rubros(models.Model):
    rubro = models.CharField(max_length=2,choices=TiposProducto.choices,default=TiposProducto.DEFAULT)    

class Persona(models.Model):
    TYPES = [(0,'PROVEEDOR'),(1,'CLIENTE')]

    rut = models.CharField(max_length=12,default="xx.xxx.xxx-x")
    nombre = models.CharField(max_length=20,default="")
    apellido = models.CharField(max_length=30,default="")
    telefono= models.IntegerField(default=999999999999)
    direccion = models.CharField(default="",max_length=50)
    tipo = models.IntegerField(choices=TYPES,default=1)

class Proveedor(Persona):
    id_proveedor = models.AutoField(primary_key=True,editable=False,default=000)
    rubro = models.ManyToManyField(Rubros,default="O")

    proveedores = models.Manager()

class Cliente(Persona):
    email = models.EmailField()

    clientes = models.Manager()

class Producto(models.Model):
    id_producto = models.CharField(primary_key=True,max_length=12)
    nombre = models.CharField(default="",max_length=50)
    descripcion = models.CharField(default="",max_length=250)
    p_compra = models.DecimalField(default=0,decimal_places=2,max_digits=12)
    p_venta = models.DecimalField(default=0,decimal_places=2,max_digits=12)
    stock = models.IntegerField(default=0)
    fecha_venc = models.DateTimeField(default="00000000")

    id_familia = models.CharField(choices=TiposProducto.choices,default='O',max_length=2)
    id_proveedor = models.ForeignKey(Proveedor,default="",on_delete=models.DO_NOTHING)
    id_ref = models.IntegerField(default=000)

    productos = models.Manager()

    def make_id(self):
        id_prov = Proveedor.proveedores.get(pk = self.id_proveedor)
        id_fam = self.id_familia
        id_prod = '{0}{1}{2}{3}'.format(id_prov,id_fam,self.fecha_venc,self.id_ref)
        return id_prod

    def save(self,*args,**kwargs):
        self.id_producto = self.make_id()
        super(Producto,self).save(*args,**kwargs)


class Boleta(models.Model):
    num_boleta = models.IntegerField(primary_key=True,default="")

class BoletaDetalle(models.Model):
    boleta = models.OneToOneField(Boleta,default="",on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto,default="",on_delete=models.DO_NOTHING)
    cantidad = models.DecimalField(default=0,decimal_places=2,max_digits=10)

class Compra(models.Model):
    STATES = [(0,'PENDIENTE'),(1,'PAGADO'),(2,'CANCELADO')]

    cliente = models.ForeignKey(Cliente,default="",on_delete=models.DO_NOTHING)
    num_boleta = models.ForeignKey(BoletaDetalle,default="",on_delete=models.DO_NOTHING)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(default=0,decimal_places=2,max_digits=9)
    #Campos adicionales

    estado = models.IntegerField(choices=STATES,default=0)

class OrdenCompra(models.Model):
    proveedor = models.OneToOneField(Proveedor,default="",on_delete=models.DO_NOTHING)
    fecha = models.DateTimeField(auto_now_add=True)

class OrdenCompraDetalle(models.Model):
    id_orden = models.OneToOneField(OrdenCompra,default="",on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto,default="",on_delete = models.CASCADE)
    cantidad = models.IntegerField(default=0)

    




