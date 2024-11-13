from django.shortcuts import render
from . models import Realisation
from django.http import FileResponse, Http404


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


def show_cv_in_pdf(request):
    try:
        return FileResponse(open("mainsite/cv_tech_n2.pdf", "rb"), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

# def contact(request):
#     """ Contact section """
#     return render(request, "mainsite/contact.html")

