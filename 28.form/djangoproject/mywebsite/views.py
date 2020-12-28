from django.shortcuts import render

from .forms import FormField


def index(request):
    form_field = FormField()

    context = {
        'heading': 'Home',
        'form_field': form_field
    }
    return render(request, 'index.html', context)
