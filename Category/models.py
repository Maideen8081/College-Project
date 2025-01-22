from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=100,unique=True, null=True,blank=True)
    category_image = models.ImageField( upload_to='photos/categories',null=True,blank=True)
    category_description = models.TextField(max_length=500,null=False,blank=False)
    
    

        
    def __str__(self):
        return self.category_name


