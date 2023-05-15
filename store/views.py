from django.shortcuts import render
from store import models
# Create your views here.

def all_products(request):
    products = models.Products.objects.all()

    context ={
        'products': products
    }

    return render(request,'store/home.html',context)


def categories(request):
    return {
        'categories': models.Category.objects.all()
    }
