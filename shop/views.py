from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Order, OrderUpdate
from math import ceil
from datetime import date, datetime
import json


def index(request):
    products = Product.objects.all()
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item["category"] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params = {'allProds': allProds}
    return render(request, "shop/index.html", params)


def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    if request.method == "POST":
        print(request)
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')
        contact = Contact(name=name, email=email, phone=phone, desc=message)
        contact.save()
    return render(request, 'shop/contact.html')


def tracker(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id=orderId, email=email)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append(
                        {'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps(
                        {"status": "success", "updates": updates, "itemsJson": order[0].items_json}, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')
    return render(request, 'shop/tracker.html')


def productview(request, myid):
    product = Product.objects.filter(id=myid)
    return render(request, 'shop/product.html', {'product': product[0]})


def checkout(request):
    if request.method == "POST":
        itemsJson = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + \
            " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        zip = request.POST.get('zip', '')
        state = request.POST.get('state', '')
        phone = request.POST.get('phone', '')
        amount = request.POST.get('amount', '')
        order = Order(name=name, email=email, phone=phone,
                      address=address, city=city, zip=zip, state=state, items_json=itemsJson, amount=amount)
        dates = date.today().strftime("%B %d,%Y")
        times = datetime.now().strftime("%H:%M:%S")

        order.save()
        update = OrderUpdate(order_id=order.order_id,
                             update_desc="Thanks for placing the Order")
        update.save()
        thank = True
        id = order.order_id
        user = {'name': name, 'email': email,
                'phone': phone, 'address': address, 'dates': dates, 'times': times, 'city': city, 'state': state}
        return render(request, 'shop/submission.html', {'thank': thank, 'id': id, 'user': user})
    return render(request, 'shop/checkout.html')
