from django.shortcuts import render

def index(request):
    title = 'Главная Страница'

    context = {
        'title': title,
    }

    return render(request, 'index.html', context)

def contacts(request):
    return render(request, 'contacts.html')

def products(request):
    return render(request, 'products.html')

def about(request):
    return render(request, 'about.html')

def product(request):
    return render(request, 'product.html')
