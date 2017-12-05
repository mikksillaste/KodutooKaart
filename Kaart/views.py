from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from Kaart import models


def index(request):
    return render(request, 'index.html')


def get_kohad(request):
    kohad = models.Kohad.objects.all().values('text', 'lat', 'lng')
    return JsonResponse(list(kohad), safe=False)
