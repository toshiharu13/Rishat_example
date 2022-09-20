from django.shortcuts import render, HttpResponse, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from .models import Item
from django.conf import settings
import stripe


def index(request):
    items = Item.objects.all
    context = {'items': items}
    return render(request, 'index.html', context=context)


def product_view(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    context = {'item': item}
    return render(request, 'product_v2.html', context=context)


@api_view(['GET'])
def get_pay(request, item_id):
    stripe.api_key = settings.STRIPE_KEY
    payload = stripe.checkout.Session.create(
        success_url="https://example.com/success",
        cancel_url="https://example.com/cancel",
        line_items=[
            {
                "price": "price_1Lk5jFADW2LfrITiNbXUJQWj",
                "quantity": 2,
            },
        ],
        mode="payment",
    )
    return Response(payload)
