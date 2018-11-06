import pandas
from stats.models import Locomotive, Mileage, Subsidiary


def load_data():
    result = True
    try:
        data = pandas.read_csv('mileage.csv', delimiter=';', header=0)
        _, _, *years = data.columns.values
        for subsidiary_name, loco_seria, *mileage_by_years in data.values:

            loco = Locomotive.objects.filter(series=loco_seria.replace(' ', '')).first()
            subsidiary = Subsidiary.objects.filter(name=subsidiary_name.replace(' ', '')).first()

            if loco and subsidiary:
                bind_loco_subsidiary(loco, subsidiary)

                load_mileage(years, subsidiary, loco, mileage_by_years)
    except BaseException as e:
        result = False
        print(e)
    finally:
        return result


def bind_loco_subsidiary(loco: Locomotive, subsidiary: Subsidiary):
    find_loco = next((l for l in subsidiary.locomotives.all() if l.series == loco.series), None)
    if not find_loco:
        subsidiary.locomotives.add(loco)
        subsidiary.save()


def load_mileage(years: list, subsidiary: Subsidiary, loco: Locomotive, mileages_by_years: list):
    for year in years:
        mileage = Mileage.objects.filter(locomotive__series=loco.series, subsidiary__name=subsidiary.name, year=year)\
            .first()
        if not mileage:
            mileage = Mileage()
            mileage.locomotive = loco
            mileage.subsidiary = subsidiary
            mileage.year = year
        mileage.value = int(mileages_by_years[years.index(year)].replace(' ', ''))
        mileage.save()