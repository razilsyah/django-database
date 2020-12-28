from django.shortcuts import render

# import forms
from .forms import kontakForm


def index(request):
    kontak_form = kontakForm()

    context = {
        'heading': 'Kontak Page',
        'kontak_form': kontak_form
    }
    return render(request, 'kontak/index.html', context)
