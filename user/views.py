from django.shortcuts import render, redirect
from .forms import ModelForm


def register(request):
    form = ModelForm
    if request.method == 'POST':
        form = ModelForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = ModelForm
    context = {
        'form': form
    }
    return render(request, 'register.html', context)