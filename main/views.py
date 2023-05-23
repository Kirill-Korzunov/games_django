from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.
menu = [
    {'title': 'Главная', 'url_name': 'home' },
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
]

def index(request):
    title = 'Главная страница'
    content = 'Главная страница'
    context = {
        'title': title,
        'menu': menu,
        'content': content,
    }
    return render(request, 'base.html', context)

def about(request):
    title = 'О сайте'
    content = 'О сайте'
    context = {
        'title': title,
        'menu': menu,
        'content': content,
    }
    return render(request, 'base.html', context)

def contact(request):
    title = 'Обратная связь'
    content = 'Обратная связь'
    context = {
        'title': title,
        'menu': menu,
        'content': content,
    }
    return render(request, 'base.html', context)

def login(request):
    title = 'Войти'
    content = 'ФОРМА ВХОДА'
    context = {
        'title': title,
        'menu': menu,
        'content': content,
    }
    return render(request, 'base.html', context)

def register(request):
    title = 'Регистрация'
    content = 'ФОРМА РЕГИСТРАЦИИ'
    context = {
        'title': title,
        'menu': menu,
        'content': content,
    }
    return render(request, 'base.html', context)

def logout_user(request):
    logout(request)
    return redirect('home')
