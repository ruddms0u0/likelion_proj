from django.shortcuts import render

def test(request):
    return render(request, 'second/test.html')
# Create your views here.
