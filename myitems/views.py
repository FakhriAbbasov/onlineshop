from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from item.models import Item

@login_required
def items(request):
    items = Item.objects.filter(created_by=request.user)

    return render(request, 'myitems/items.html', {
        'items': items,
    })



