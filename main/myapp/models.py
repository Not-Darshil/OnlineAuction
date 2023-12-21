from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=256,null=False)
    brand=models.CharField(max_length=256,null=False)
    start_bid=models.IntegerField(null=False)
    description=models.CharField(max_length=512)
    image=models.ImageField(upload_to='myapp/images',null=False)
    date=models.DateField(auto_now_add=True)

