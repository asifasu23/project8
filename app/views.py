from django.shortcuts import render

# Create your views here.

def shamsheer(request):
    d={'name':'shaik shamsheer'}
    return render(request,'shamsheer.html',d)