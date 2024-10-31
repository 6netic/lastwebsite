from django.shortcuts import render
from . models import Realisation


def home(request):
    """ Homepage of 6netic website """
    return render(request, "mainsite/index.html")


def realisations(request):
    """ Projects section """
    context = {'realisations': Realisation.objects.all()}
    return render(request, "mainsite/realisations.html", context=context)


def services(request):
    """ Services section """
    return render(request, "mainsite/services.html")


# def contact(request):
#     """ Contact section """
#     return render(request, "mainsite/contact.html")

