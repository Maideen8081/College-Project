from django .shortcuts import render
from Store.models import Products



def home(request):
    
    product=Products.objects.all().filter(is_available=True)
    context ={
        'product':product,
    }
   
    return render(request,"home.html",context)