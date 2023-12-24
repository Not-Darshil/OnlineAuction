from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=256,null=False)
    brand=models.CharField(max_length=256,null=True, default="")
    category = models.CharField(max_length=50, blank=True, null=True, default="")
    description=models.CharField(max_length=512,default="",null=True)
    start_bid=models.DecimalField(max_digits=10, decimal_places=2)
    image=models.ImageField(upload_to='myapp/images',null=False)
    lister=models.ForeignKey(User, on_delete=models.CASCADE,null=False)
    date=models.DateField(default=now, editable=False)

    def __str__(self):
        return self.name

    # class Bidding(models.Model):
    #     bidder = models.CharField(max_length=50, blank=True, null=True)
    #     bidprice = models.DecimalField(max_digits=15, decimal_places=2)
    #     listingid = models.IntegerField()

    #     def __str__(self):
    #         return f"{self.listingid}"


