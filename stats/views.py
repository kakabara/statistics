from django.shortcuts import render
from django.http import JsonResponse, HttpRequest

from .models import Mileage
from stats.data import load_data
# Create your views here.


def loader(request: HttpRequest):
    result = load_data()
    loading_result = {'result': result}
    return JsonResponse(loading_result)


def index(request: HttpRequest):
    return render(request, '../templates/index.html')


def stats(request: HttpRequest):
    filters = request.POST.get('filters', {})
    mileages = None
    mileages = Mileage.objects.filters(**filters).all()
    data = {
        'stats':
            {}
    }
    return JsonResponse(data)
