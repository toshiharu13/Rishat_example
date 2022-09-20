from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Item


def index(request):
    items = Item.objects.all
    context = {'items': items}
    return render(request, 'index.html', context=context)


def product_view(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    context = {'item': item}
    return render(request, 'product.html', context=context)
