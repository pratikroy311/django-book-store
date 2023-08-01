

from decimal import Decimal
from store.models import Products


class Basket():
    def __init__(self, request):
        self.session=request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey']={
                
            }
        self.basket = basket

    def add(self,product,qty):
        product_id = str(product.id)
        if product_id in self.basket:
            self.basket[product_id]['qty']=qty
        else:
            self.basket[product_id]={
                'price': str(product.price),
                'qty':int(qty)}

        self.session['skey'] = self.basket
        self.save()

    def __len__(self):
        """ get the basket data and count the qty of items"""
        return sum(item['qty'] for item in self.basket.values())
    
    def __iter__(self):
        product_ids = self.basket.keys()
        products= Products.products.filter(id__in=product_ids)
        basket = self.basket.copy()

        for product in products:
            basket[str(product.id)]['product']=product

        for item in basket.values():
            item['price']= Decimal(item['price'])
            item['total_price'] = item['price']*item['qty']
            yield item
    
    def get_total_price(self):
        return sum(Decimal(item['price'])*item['qty'] for item in self.basket.values())
    
    def delete(self,product):
        product_id = str(product)
        if product_id in self.basket:
            del self.basket[product_id]
            self.save()
    
    def update(self,product,qty):
        product_id= str(product)
        qty= qty
        if product_id in self.basket:
            self.basket[product_id]['qty']= int(qty)
        self.save()

    def save(self):
        self.session.modified= True
        

