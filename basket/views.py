from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from store.models import Products
from .basket import Basket


def basket_summary(request):
    basket= Basket(request)
    return render(request,'store/basket/summary.html',{'basket':basket})

def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action')== 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Products,id=product_id)
        basket.add(product=product,qty=product_qty)
        basket_qty = basket.__len__()
        response = JsonResponse({'qty':basket_qty})
        return response