from django.shortcuts import render

from mainapp.models import Product


def index(request):
    title = 'Главная Страница'

    prods = Product.objects.all()[:4]

    context = {
        'title': title,
        'products': prods
    }

    return render(request, 'index.html', context)

def contacts(request):
    title = 'Контакты'
    context = {
        'title': title,
    }
    return render(request, 'contacts.html', context)

def products(request):
    prods = Product.objects.all()[:3]
    title = 'Товары'
    context = {
        'title': title,
        'products': prods
    }
    return render(request, 'products.html', context)

def about(request):
    title = 'О Нас'
    context = {
        'title': title,
    }
    return render(request, 'about.html', context)

def product(request):
    prods = Product.objects.all()[:4]
    title = 'Товар'

    context = {
        'title': title,
        'products': prods
    }
    return render(request, 'product.html', context)
