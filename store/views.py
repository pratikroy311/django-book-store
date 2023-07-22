from django.shortcuts import render,get_object_or_404
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

def product_detail(request,slug):
    product = get_object_or_404(models.Products,slug=slug,in_stock=True)
    return render(request,'store/products/detail.html',{'product':product})


