from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .forms import SearchForm
from sozluk.models import Sozcukler, Sesler, Diller

# Create your views here.

# def search(request, search_term):
#     if request.method == 'POST':
#         form = SearchForm(request.POST)
#         if form.is_valid():
#             query = form.cleaned_data['query']
#             results = Sozcukler.objects.filter(sozcuk__icontains=query)
#             return render(request, 'sozluk/search_results.html', {'results': results})
#     else:
#         form = SearchForm()
#     return render(request, 'sozluk/search.html', {'form': form})

def search(request):
    context = {
        "sesler": Sesler.objects.all()
    }
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            return redirect('search_results', search_term=query)
    else:
        form = SearchForm()
    context['form'] = form
    return render(request, 'sozluk/search.html', context)

def search_results(request, search_term):
    context = {
        "sesler": Sesler.objects.all(),
        "diller": Diller.objects.all()
    }
    results = Sozcukler.objects.filter(sozcuk__icontains=search_term)
    context['results'] = results
    return render(request, 'sozluk/search_results.html', context)

def index(request):
    context = {
        "sesler": Sesler.objects.all(),
        "diller": Diller.objects.all()
    }
    return render(request, "sozluk/index.html", context)

def bilgilendirme(request):
    context = {
        "sesler": Sesler.objects.all()
    }
    return render(request, "sozluk/о_словаре.html", context)

def sozcukler(request):
    context = {
        "icerikler": Sozcukler.objects.all(),
        "sesler": Sesler.objects.all(),
        "diller": Diller.objects.all(),
    }
    return render(request, "sozluk/sozcukler.html", context)

def icerik(request, slug):
    sozcuk = Sozcukler.objects.get(slug=slug)
    context = {
        "sesler": Sesler.objects.all(),
        "sozcuk": sozcuk
    }
    return render(request, "sozluk/icerik.html", context)

def seslere_gore_sozcukler(request, slug):
    context = {
        "icerikler": Sozcukler.objects.filter(ses__slug=slug),
        "sesler": Sesler.objects.all(),
        "basliklar": Sesler.objects.filter(slug=slug)
    }
    return render(request, "sozluk/sozcukler.html", context)

def dillere_gore_sozcukler(request, slug):
    context = {
        "icerikler": Sozcukler.objects.filter(dil__slug=slug),
        "diller": Diller.objects.all(),
        "sesler": Sesler.objects.all()
    }
    return render(request, "sozluk/sozcukler.html", context)