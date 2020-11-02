from django.urls import path
from .views import home,showProducts,addProduct,addPoveedor, login_user, logout_user

urlpatterns=[
    path('',home,name='home'),
    path('Products/',showProducts,name='products'),
    path('Products/add/',addProduct,name='addproduct'),
    #path('Proveedor/'),
    path('Proveedor/add/',addPoveedor,name='addproveedor'),
    path('Auth/Login',login_user,name='login'),
    path('Logout/',logout_user,name='logout')
]