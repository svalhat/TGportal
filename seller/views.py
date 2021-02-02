from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader


def seller(request):
    return render(request,'seller/seller.html')
def sellerprofile(request):
    return render(request,'seller/sellerprofile.html')
def orderidseller(request):
    return render(request,'seller/orderidseller.html')
def sellerorder(request):
    return render(request,'seller/sellerorder.html')

def updatepassword(request):
    context = {'segment': 'update_password'}
    html_template = loader.get_template('seller/update password.html')

    return HttpResponse(html_template.render(context, request))
