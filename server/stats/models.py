from django.db import models
from django.core.validators import MinValueValidator


class Locomotive(models.Model):
    series = models.CharField(max_length=100)
    rate_per_km = models.FloatField(MinValueValidator(0))


class Subsidiary(models.Model):
    name = models.CharField(max_length=40)
    locomotives = models.ManyToManyField(Locomotive, blank=True)


class Mileage(models.Model):
    class Meta:
        unique_together = (('locomotive', 'subsidiary', 'year'), )

    locomotive = models.ForeignKey(Locomotive, on_delete=models.DO_NOTHING)
    subsidiary = models.ForeignKey(Subsidiary, on_delete=models.DO_NOTHING)
    year = models.IntegerField(validators=[MinValueValidator(2000)], default=2000)
    value = models.IntegerField(MinValueValidator(0))
