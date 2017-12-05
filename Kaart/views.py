from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from Kaart import models
from Kaart.models import Kohad


def index(request):
    return render(request, 'index.html')


def get_kohad(request):
    kohad = models.Kohad.objects.all().values('text', 'lat', 'lng')
    return JsonResponse(list(kohad), safe=False)


def add_koht(request):
    if request.is_ajax():
        if request.method == 'GET':
            kohad = Kohad()
            kohad.text = request.GET.get('text')
            kohad.lat = request.GET.get('lat')
            kohad.lng = request.GET.get('lng')
            kohad.save()
            return render(request, 'index.html')
