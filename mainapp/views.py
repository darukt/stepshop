from django.shortcuts import render

from mainapp.models import Product, Category


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
    prods = Product.objects.all()[:6]

    categories = Category.objects.all()

    title = 'Товары'

    context = {
        'title': title,
        'products': prods,
        'categories': categories,
    }

    return render(request, 'products.html', context)

def about(request):
    title = 'О Нас'
    context = {
        'title': title,
    }
    return render(request, 'about.html', context)

def product(request):
    prods = Product.objects.all()[:5]
    title = 'Товар'

    prod = Product.objects.get(pk=1)

    context = {
        'title': title,
        'products': prods,
        'prod': prod
    }
    return render(request, 'product.html', context)
