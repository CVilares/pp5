from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OfCceDMa3ROsIUzXFB6RB2WUcY2S0lQKbmth0rAnt7m3Tu4C6w0t4XuRNCufTpXLarc0KH8coT6LutuSiPsfP9Y001PskljP9',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
