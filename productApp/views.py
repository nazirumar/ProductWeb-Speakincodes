
from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    products=Products.objects.all()
    context={
        'products':products
    }
    return render(request, 'index.html', context)