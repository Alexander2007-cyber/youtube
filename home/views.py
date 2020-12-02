from django.shortcuts import render
from .models import AddedVideo

def home(request):
    data = AddedVideo.objects.all()
    context = {
        'qs': data
    }
    return render(request, 'index.html', context)


def watch(request, code):
    return render(request, 'watch.html')