from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def edit(request):
    return render(request, 'edit.html')

# Create your views here.
