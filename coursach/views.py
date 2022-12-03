from django.shortcuts import render, redirect
from .forms import *
from .models import *


def home(request):
    tours = Tour.objects.all()

    return render(request, 'home.html', {'tours': tours})

def create(request, pk):
    errors = ''
    if request.POST:
        tour_form = TourForm(request.POST)
        if tour_form.is_valid():
            tour_form.save()

            petition = TourPetition.objects.last()
            petition.tour = Tour.objects.get(pk=pk)
            petition.save()
            return redirect('/')
        else:
            errors = tour_form.errors
    else:
        tour_form = TourForm

    return render(request, 'create.html', {'form': tour_form, 'errors': errors})
