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
        response['loco'][loco.id] = {
            'series': loco.series
        }

    for sub in all_subsidiaries:
        response['subsidiary'][sub.id] = {
            'name': sub.name,
            'locomotives': [l.id for l in sub.locomotives.all()]
        }

    return JsonResponse(response)


def index(request: HttpRequest):
    return render(request, '../templates/index.html')


def loader(request: HttpRequest):
    result = load_data()
    loading_result = {'result': result}
    return JsonResponse(loading_result)


def stats(request: HttpRequest):
    filters = dict(request.GET)
    filters = {k: filters[k][0] for k in filters}
    mileages = None
    mileages = Mileage.objects.filter(**filters).all()
    data = {
        'stats':
            []
    }
    if len(mileages):
        stats_by_year = {}
        for mileage in mileages:
            stats_by_year.setdefault(mileage.year, []).append(mileage.value * mileage.locomotive.rate_per_km)

        for year in stats_by_year:
            sum_by_year = stats_by_year[year]
            stats_by_year[year] = sum(sum_by_year)
        data['stats'] = [{'x': year, 'y': stats_by_year[year]} for year in stats_by_year]
        data['labels'] = list(stats_by_year.keys())
    return JsonResponse(data)
