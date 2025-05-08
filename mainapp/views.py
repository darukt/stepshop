from django.shortcuts import render

def index(request):
    title = 'Главная Страница'

    context = {
        'title': title,
    }

    return render(request, 'index.html', context)

def contacts(request):
    title = 'Контакты'
    context = {
        'title': title,
    }
    return render(request, 'contacts.html', context)

def products(request):
    title = 'Продукты'
    context = {
        'title': title,
    }
    return render(request, 'products.html', context)

def about(request):
    title = 'О Нас'
    context = {
        'title': title,
    }
    return render(request, 'about.html', context)

def product(request):
    title = 'Продукт'
    context = {
        'title': title,
    }
    return render(request, 'product.html', context)
