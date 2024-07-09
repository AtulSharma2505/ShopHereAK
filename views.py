from django.shortcuts import render

from .models import Product,Contact
from math import ceil

# Create your views here.
from django.http import HttpResponse

def index(request):
    #products = Product.objects.all()
    #print(products)
    #n = len(products)
    #nSlides = n//4 + ceil((n/4)-(n//4))
    allProds = []
    catprods = Product.objects.values('cateogory','id')
    cats = {item['cateogory'] for item in catprods}
    for cat in cats:
        products = Product.objects.filter(cateogory=cat)
        n = len(products)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([products,range(1,nSlides),nSlides])
    #allProds = [[products,range(1, nSlides), nSlides],
              # [products,range(1, nSlides), nSlides]]
    params = {'allProds':allProds}
    return render(request, 'shop/index.html',params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    if request.method == "POST":
        name= request.POST.get('name','')
        email= request.POST.get('email','')
        phone= request.POST.get('phone','')
        desc= request.POST.get('desc','')
        contact= Contact(name=name ,email=email ,phone=phone ,desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def prodView(request, myid):
    products = Product.objects.filter(id = myid)
    return render(request, 'shop/prodView.html', {'products':products[0]})


def checkout(request):
    return render(request, 'shop/checkout.html')