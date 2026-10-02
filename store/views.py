from django.shortcuts import render
from .data.menu_data import menu_data


def home(request):
    return render(
        request,
        'index.html',
        {
            'products': menu_data
        }
    )