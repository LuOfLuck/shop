from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import json
# Create your views here.
def store(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.ordenitem_set.all()
        cartItem = order.get_total_item
    else:
        items = []
        order = {"get_total_item":0, "get_total_orden":0}
        cartItem = order["get_total_orden"]
    
    products = Product.objects.all()
    context = {"products": products, "cartItem": cartItem}
    return render(request, "store/store.html", context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.ordenitem_set.all()
        cartItem = order.get_total_item
    else:
        items = []
        order = {"get_total_item":0, "get_total_orden":0}
        cartItem = order["get_total_orden"]
    context = {"items":items, "order":order,"cartItem": cartItem}
    return render(request, "store/cart.html", context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.ordenitem_set.all()
        cartItem = order.get_total_item
    else:
        items = []
        order = {"get_total_item":0, "get_total_orden":0}
        cartItem = order["get_total_orden"]
    context = {"items":items, "order":order,"cartItem": cartItem}
    return render(request, "store/checkout.html", context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print("productId:", productId)
    print("action:", action)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    ordenItem, created = OrdenItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        ordenItem.quantity += 1
    elif action == 'remove':
        ordenItem.quantity -= 1

    ordenItem.save()

    if ordenItem.quantity <= 0:
        ordenItem.delete()

    return JsonResponse("Item was added", safe=False)



'''

<?php

function prueba(){

    x = 10
    y = 15
    z = [x, y, f,SD,S,D,S,D,,SD,S,A,D,ASD,A,S]
    return z

}

$var = prueba()
$x = var[0]
$y = var[1]
foreach ($var as $i) { //guarda de forma autonumerica el valor de $var en $i
    echo $i; //muestra $i
}

?>x
[10, 15]

'''