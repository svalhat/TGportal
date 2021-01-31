from django.db import models

# Create your models here.
class UserReg(models.Model):
    user_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=20)
    Mobile_no= models.BigIntegerField(unique=True)
    Whatsapp_no=models.BigIntegerField(unique=True)
    Email_id= models.EmailField()
    City=models.CharField(max_length=10)
    Password= models.CharField(max_length=20)
    RepeatPassword=models.CharField(max_length=20)
    Are_you_Seller=models.CharField(max_length=10)
    def __str__(self):
        return self.email
