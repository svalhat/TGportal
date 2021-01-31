from django.shortcuts import render

# Create your views here.

def Buyer(request):
    return render(request,'buyer/buyer.html')
def orderidbuyer(request):
    return render(request,'buyer/orderidbuyer.html')
def buyerprofile(request):
    return render(request,'buyer/buyerprofile.html')