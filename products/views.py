from django.shortcuts import render

# Create your views here.
def all_products(request):
    """a view to show all product, including sorting and queries"""

    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)