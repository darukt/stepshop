from django.shortcuts import render, get_object_or_404

from mainapp.models import Product, Category

from basketapp.models import Basket

from mainapp.utils import get_main_menu, get_basket

def index(request):
    title = 'Главная Страница'

    prods = Product.objects.all()[:4]
    basket = []

    if request.user.is_authenticated:
        basket = get_basket(request.user)

    context = {
        'title': title,
        'products': prods,
        'menu_links': get_main_menu(),
        'basket': basket,
    }

    return render(request, 'index.html', context)

def contacts(request):
    title = 'Контакты'
    basket = []
    if request.user.is_authenticated:
        basket = get_basket(request.user)
    context = {
        'title': title,
        'menu_links': get_main_menu('mainapp:contacts'),
        'basket': basket,
    }
    return render(request, 'contacts.html', context)

def products(request, pk=None):
    prods = Product.objects.all()[:6]

    categories = Category.objects.all()

    basket = []

    if request.user.is_authenticated:
        basket = get_basket(request.user)

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
    basket = []
    if request.user.is_authenticated:
        basket = get_basket(request.user)
    context = {
        'title': title,
        'menu_links': get_main_menu('mainapp:about'),
        'basket': basket,
    }
    return render(request, 'about.html', context)

def product(request, pk):
    title = 'Товар'
    basket = []
    prod = Product.objects.get(pk=pk)
    prods = Product.objects.exclude(id=pk)


    if request.user.is_authenticated:
        basket = get_basket(request.user)

    context = {
        'title': title,
        'prod': prod,
        'products': prods,
        'menu_links': get_main_menu('mainapp:products'),
        'basket': basket,
    }
    return render(request, 'product.html', context)
