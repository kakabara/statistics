from django.shortcuts import render
from django.http import JsonResponse, HttpRequest

from .models import Mileage, Subsidiary, Locomotive
from stats.data import load_data
from django.views.decorators.csrf import csrf_exempt

import json


# Create your views here.


def get_info(request: HttpRequest):
    all_loco = Locomotive.objects.all()
    all_subsidiaries = Subsidiary.objects.all()
    all_mileage = Mileage.objects.all()
    all_years = [m.year for m in all_mileage]
    min_year = min(all_years)
    max_year = max(all_years)

    response = {
        'loco': {},
        'subsidiary': {},
        'min_year': min_year,
        'max_year': max_year
    }

    for loco in all_loco:
        response['loco'][loco.id] = {
            'series': loco.series
        }

    for sub in all_subsidiaries:
        response['subsidiary'][sub.id] = {
            'name': sub.name,
            'locomotives': [l.id for l in sub.locomotives.all()],
        }

    return JsonResponse(response)


def index(request: HttpRequest):
    return render(request, '../templates/index.html')


def loader(request: HttpRequest):
    result = load_data()
    loading_result = {'result': result}
    return JsonResponse(loading_result)


@csrf_exempt
def stats(request: HttpRequest):
    body = json.loads(request.body.decode('utf-8'))
    filters = list(body.get('filters', []))
    time_range = body.get('time_range', {})
    mileages_query = None
    for f in filters:
        if not mileages_query:
            mileages_query = Mileage.objects.filter(**f)
        else:
            mileages_query = Mileage.objects.filter(**f) or mileages_query
        mileages_query = mileages_query.filter(**time_range)

    if mileages_query is None:
        mileages = []
    else:
        mileages = mileages_query.all()

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
