from django.shortcuts import render, redirect
from django.contrib.auth import logout
from item.models import Category, Item
from django.db.models import Q
from .forms import SignupForm

def items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold = False)

    if category_id:
        items = items.filter(category_id=category_id)

    if query: 
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    context = {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id)
    }

    return render(request, 'core/items.html', context)

def categories(request):
    categories = Category.objects.all()
    return render(request, 'core/categories.html', {
        'categories': categories,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

def user_logout(request):
    logout(request)
    return redirect('/')