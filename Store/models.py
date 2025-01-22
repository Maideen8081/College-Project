from django.db import models
from Category.models import Category

class Products(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100,null=False)
    slug=models.SlugField(max_length=100,unique=True)
    product_image = models.ImageField(upload_to='photos/products',null=False)
    price=models.IntegerField(null=False,blank=False)
    description = models.CharField(max_length=500,null=False,blank=False)
    stock = models.IntegerField(null=False,blank=False)
    is_available=models.BooleanField(default=True)
    create_date=models.DateTimeField(auto_now_add=True)
    modifie_dated=models.DateTimeField(auto_now=True)
    
    
    
    def __str__(self):
        return self.product_name 
