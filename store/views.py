from django.shortcuts import render,get_object_or_404
from store import models
# Create your views here.

def product_all(request):
    products = models.Products.products.all()[:50]
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
    return render(request,'store/products/product.html',{'product':product})

def category_list(request,category_slug):
    category = get_object_or_404(models.Category,slug=category_slug)
    products = models.Products.objects.filter(category=category)
    return render(request,'store/products/category.html',{"category":category,"products":products})


