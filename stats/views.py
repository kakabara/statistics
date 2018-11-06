from django.shortcuts import render
from django.http import JsonResponse, HttpRequest

from .models import Mileage, Subsidiary, Locomotive
from stats.data import load_data
# Create your views here.


def get_info(request: HttpRequest):
    response = {
        'loco': {},
        'subsidiary': {}
    }
    all_loco = Locomotive.objects.all()
    all_subsidiaries = Subsidiary.objects.all()

    for loco in all_loco:
        response['loco'][loco.id] = loco.series

    for sub in all_subsidiaries:
        response['subsidiary'][sub.id] = {
            'name': sub.name,
            'locomotives': [l.series for l in sub.locomotives.all()]
        }

    return JsonResponse(response)


def index(request: HttpRequest):
    return render(request, '../templates/index.html')


def loader(request: HttpRequest):
    result = load_data()
    loading_result = {'result': result}
    return JsonResponse(loading_result)


def stats(request: HttpRequest):
    filters = request.POST.get('filters', {})
    mileages = None
    mileages = Mileage.objects.filters(**filters).all()
    data = {
        'stats':
            {}
    }
    return JsonResponse(data)
