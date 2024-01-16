from django.shortcuts import render

# Create your views here.

def index(request):
    """to return index pag"""
    return render(request, 'home/index.html')
