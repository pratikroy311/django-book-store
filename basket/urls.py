from django.urls import path
from basket import views

app_name = 'basket'
urlpatterns =[
    path('',views.basket_summary, name="basket_summary"),
]