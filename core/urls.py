# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
import buyer,seller
import gui
from gui import views
from seller import views

from buyer import views


from Product import views




# add this

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
   # path('admin' , admin.site.urls),          # Django admin route
    path("", include("authentication.urls")), # Auth routes - login / register
    url("", include("app.urls")),             # UI Kits Html files
    #path('contact/', views.contact),
   # path('', include('contact.urls')),
   # path('Product/', views.contact),
    #path('', include('Product.urls'))
   # path('Product/', views.ProductList.as_view()),  # Django admin route
    #path('Products/', views.ProductList.as_view()),  # Django admin route
    path('addeditproduct/', views.Product1),
    path('', include('Product.urls')),

    path('ProductHome/', views.ProductHome),
    path('', include('Product.urls')),
   # path('sellerorder/', views.sellerorder),
    #path('', include('Product.urls')),
    #path('vieworderidseller/', views.vieworderidseller),
    #path('', include('Product.urls')),
   # path('buyer/', views.Buyer),
    #path('', include('Product.urls')),
   # path('vieworderidbuyer/', views.orderidbuyer),
    #path('', include('Product.urls')),
    #path('buyerprofile/', views.buyerprofile),
    #path('', include('Product.urls')),
    #path('seller/', views.seller),
    #path('', include('Product.urls')),
    #path('sellerprofile/', views.sellerprofile),
    #path('', include('Product.urls')),
    path('base/',gui.views.base),
    path('login',gui.views.login,name='login'),
    path('sign_up',gui.views.sign_up,name='sign_up'),
    path('Dashboard/', views.Dashboard),
    path('buyer/', buyer.views.Buyer),
    path('buyerprofile/', buyer.views.buyerprofile),
    path('orderidbuyer/',buyer.views.orderidbuyer),
    path('seller/', seller.views.seller),
    path('sellerprofile/', seller.views.sellerprofile),
    path('sellerorder/', seller.views.sellerorder),
    path('orderidseller/',seller.views.orderidseller),
    path('update password', seller.views.updatepassword, name='update password'),

]

