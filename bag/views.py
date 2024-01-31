from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """to return bag pag"""
    return render(request, 'bag/bag.html')