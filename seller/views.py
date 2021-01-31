from django.shortcuts import render

# Create your views here.
def seller(request):
    return render(request,'seller/seller.html')
def sellerprofile(request):
    return render(request,'seller/sellerprofile.html')
def orderidseller(request):
    return render(request,'seller/orderidseller.html')
def sellerorder(request):
    return render(request,'seller/sellerorder.html')
