from django.shortcuts import render
from rembg import remove
from PIL import Image
import os
from django.core.files.storage import FileSystemStorage

def home(request):

    context = {}

    return render(request, 'store/home.html',context)

def store(request):

    context = {}

    return render(request, 'store/store.html',context)

def cart(request):

    context = {}
    
    return render(request, 'store/cart.html',context)

def checkout(request):

    context = {}
    
    return render(request, 'store/checkout.html',context)