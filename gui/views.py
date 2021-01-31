from sqlite3 import IntegrityError

from django.shortcuts import render

# Create your views here.
from gui.models import UserReg


def base(request):
    return render(request,'gui/base.html')
def login(request):
    return render(request,'gui/login.html')
def sign_up(request):

   try:

        if request.method == "POST":
            user = UserReg()
            user.username=request.POST['username']
            user.Mobile_no=request.POST['Mobile_no']
            user.Whatsapp_no = request.POST['Whatsapp_no']
            user.Email_id = request.POST['Email_id']
            user.City=request.POST['City']
            user.Password = request.POST['Password']
            user.RepeatPassword=request.POST['Repassword']
            user.Are_you_Seller=request.POST['Are_You_Seller']
            user.save()
   except IntegrityError:
        return render(request,'gui/login.html')
   return render(request,'gui/sign_up.html')