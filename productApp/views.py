
from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):

    category =request.GET.get('category')
    if category == None:
        photos =ProductImage.objects.all()
    else:
        photos=ProductImage.objects.filter(category__CategoryName=category)


    categories= Category.objects.filter()
    products=Products.objects.all()
    context={ 
        'products':products,
        'categories':categories,
        'photos':photos
    }
    return render(request, 'index.html', context)