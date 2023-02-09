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

def removal(request):

    if request.method == 'POST' and request.FILES['upload']:
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)

        input_path = fss.path(file)
        output_path = 'static/images/output.png'

        input = Image.open(input_path)
        output = remove(input)
        output.save(output_path)
        
        file_url = fss.url('static/images/output.png')
        os.remove(fss.path(file))
        
        return render(request, 'store/store.html', {'file_url': file_url})

    return render(request,'store/store.html',{})

def cart(request):

    context = {}
    
    return render(request, 'store/cart.html',context)

def checkout(request):

    context = {}
    
    return render(request, 'store/checkout.html',context)