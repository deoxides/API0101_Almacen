from django.shortcuts import render,HttpResponseRedirect, redirect
from django.template import RequestContext
from django.core.exceptions import PermissionDenied
from django.contrib.auth import authenticate, login, logout
from .models import Producto
from .forms import ProductoAdmin, LoginForm, ProveedorAdmin

# Create your views here.
def login_user(request):
    msg =[]
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect(home)
            else:
                msg.append('Usuario o contraseña incorrectos')
                form = LoginForm()
                return render(request,'Almacen/complements/login.html',{'form':form,'errors':msg})
        else:
            msg.append(form.errors)
    else:
        form = LoginForm()
        return render(request,'Almacen/complements/login.html',{'form':form})

def logout_user(request):
    logout(request)
    form = LoginForm()
    return render(request,'Almacen/complements/login.html',{'form':form})

def home(request):
    if request.user.is_staff:
        return render(request,'Almacen/app_index.html')
    else:
        raise PermissionDenied  

#Product views
def showProducts(request):
    products = Producto.productos.all()
    return render(request,'Almacen/show_products.html',{'objects':products})

def addProduct(request):
    msg = []
    if request.method == 'POST':
        form = ProductoAdmin(request.POST)
        if form.is_valid():
            
            form.save(commit=False)
            return HttpResponseRedirect('/added/')
        else:
            msg.append(form.errors)
            return render(request,'',{'form':form,'errors': msg})
    else:
        form = ProductoAdmin()
        action_url = 'addproduct'
        form_name = 'Agregar un producto'
        context = {'form':form,'action_url':action_url,'form_name':form_name}
    return render(request, 'Almacen/forms.html', context)

#Proveedor views
def showProveedores(request):
    pass

def addPoveedor(request):
    msg = []
    if request.method == 'POST':
        form = ProveedorAdmin(request.POST)
        if form.is_valid():
            
            form.save(commit=False)
            return HttpResponseRedirect('/added/')
        else:
            msg.append(form.errors)
            return render(request,'',{'form':form,'errors': msg})
    else:
        form = ProveedorAdmin()
        action_url = 'addproveedor'
        form_name = 'Agregar un proveedor'
        context = {'form':form,'action_url':action_url,'form_name':form_name}
    return render(request, 'Almacen/forms.html', context)


#Error handling
def handler404(request, exception):
    err_code = 404
    err_msg = 'No se encuentra el sitio'
    error = {'code':err_code,'message':err_msg}
    response = render(request,'Almacen/complements/error.html',{'error':error})
    response.status_code = 404
    return response

def handler403(request, exception):
    err_code = 403
    err_msg = 'No tiene permisos para acceder a este sitio'
    error = {'code':err_code,'message':err_msg}
    options = {'suggest':'Ingresar como administrador','help_link':'login'}
    context ={'error':error,'options':options}
    response = render(request,'Almacen/complements/error.html',context)
    response.status_code = 403
    return response
