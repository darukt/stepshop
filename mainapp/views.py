from django.shortcuts import render, get_object_or_404

from mainapp.models import Product, Category

from basketapp.models import Basket

def get_main_menu(current='mainapp:index'):
    return  [
        {'href': 'mainapp:index', 'name': 'Главная', 'active': current},
        {'href': 'mainapp:products', 'name': 'Товары', 'active': current},
        {'href': 'mainapp:about', 'name': 'О Нас', 'active': current},
        {'href': 'mainapp:contacts', 'name': 'Контакты', 'active': current},
    ]

def little_menu_link(current='mainapp:products'):
    return [
        {'href': 'product:category', 'name': 'Все', 'active': current},
        {'href': 'product:category', 'name': 'Джинсы', 'active': current},
        {'href': 'product:category', 'name': 'Кеды', 'active': current},
        {'href': 'product:category', 'name': 'Сумки', 'active': current},
    ]

def index(request):
    title = 'Главная Страница'

    prods = Product.objects.all()[:4]

    context = {
        'title': title,
        'products': prods,
        'menu_links': get_main_menu(),
    }

    return render(request, 'index.html', context)

def contacts(request):
    title = 'Контакты'
    context = {
        'title': title,
        'menu_links': get_main_menu('mainapp:contacts'),
    }
    return render(request, 'contacts.html', context)

def products(request, pk=None):
    prods = Product.objects.all()[:6]

    categories = Category.objects.all()

    basket = []

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    title = 'Товары'

    context = {
        'title': title,
        'products': prods,
        'categories': categories,
        'menu_links': get_main_menu('mainapp:products'),
        'basket': basket,
    }

    if pk is not None:
        if pk == 0:
            products_ = Product.objects.all()
            category = {'name': "Все"}
        else:
            category = get_object_or_404(Category, pk=pk)
            products_ = Product.objects.filter(category__pk=pk)

        context.update({'products': products_, 'category': category})

    return render(request, 'products.html', context)

def about(request):
    title = 'О Нас'
    context = {
        'title': title,
        'menu_links': get_main_menu('mainapp:about')
    }
    return render(request, 'about.html', context)

def product(request, pk):
    title = 'Товар'

    prod = Product.objects.get(pk=pk)
    prods = Product.objects.exclude(id=pk)

    context = {
        'title': title,
        'prod': prod,
        'products': prods,
        'menu_links': get_main_menu('mainapp:products')
    }
    return render(request, 'product.html', context)
