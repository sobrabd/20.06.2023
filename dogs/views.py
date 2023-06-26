from django.shortcuts import render
from .models import Dog, Spice


def index(request):
    context = {
        "spicies": Spice.objects.all()[:3]
    }
    return render(request, 'dogs/index.html', context)


def dog_spiceis(request, pk):
    context = {
        "dogs": Dog.objects.filter(specie=pk)
    }
    return render(request, 'dogs/dog_spiceies.html', context)