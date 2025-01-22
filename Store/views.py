from django.shortcuts import render
from .models import Products


def store(request):
    product=Products.objects.all().filter(is_available=True)
    context ={
        'product':product,
        }
    
    return render (request,"store.html",context)



def cart(request):
    return render(request,"Carts/cart.html")



