from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .forms import newItemForm, editItemForm
from .models import Item, Basket, BasketItem

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:6]
    context = {
        'item': item,
        'related_items': related_items,
    }
    return render(request, 'item/detail.html', context)

@login_required
def new(request):
    form = newItemForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        item = form.save(commit=False)
        item.created_by = request.user
        item.save()
        return redirect('item:detail', pk=item.id)

    context = {
        'form': form,
        'title': 'New item',
    }
    return render(request, 'item/form.html', context)

@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    
    form = editItemForm(request.POST or None, request.FILES or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('item:detail', pk=item.id)

    context = {
        'form': form,
        'title': 'Edit item',
    }

    return render(request, 'item/form.html', context)

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    return redirect('myitems:items')

@login_required
def view_basket(request):
    basket, _ = Basket.objects.get_or_create(user=request.user)
    basket_items = BasketItem.objects.filter(basket=basket)
    return render(request, 'item/basket.html', {'basket_items': basket_items})

@login_required
def add_to_basket(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    basket, _ = Basket.objects.get_or_create(user=request.user)
    _, created = BasketItem.objects.get_or_create(item=item, basket=basket)
    if not created:
        BasketItem.objects.create(item=item, basket=basket)
    return redirect('/')

@login_required
def remove_from_basket(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    basket = Basket.objects.filter(user=request.user).first()
    if basket: 
        basket.items.remove(item)
    return redirect('/')