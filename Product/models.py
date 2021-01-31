from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Product(models.Model):

    Productid = models.IntegerField(default=0)
    # Userid =  models.ForeignKey(Category, on_delete=models.CASCADE, default=1, related_name="User_id")
    # Categoryid =  models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.TextField(max_length=500, null=True)
    Photos = models.ImageField(upload_to='main_product/', blank=True, null=True)
    GST = models.FloatField(max_length=100, null=True)
    # Courier_self = models.BooleanField(null=True)
    self_Deliverycost = models.DecimalField(max_digits=10, decimal_places=5, null=True)
    # Delivery_Parteners_id= models.ForeignKey(Category, on_delete=models.CASCADE, default=1,related_name="User_id")
    Length = models.FloatField(max_length=100, null=True)
    Width = models.FloatField(max_length=100, null=True)
    Height = models.FloatField(max_length=100, null=True)
    Delivery_Parteners_cost = models.IntegerField(null=True)
    Productcost = models.IntegerField(null=True)
    status = models.TextField(max_length=500, null=True)




