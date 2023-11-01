from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(unique=True)
    contact_details = models.CharField()


class MeterModel(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    model_name = models.CharField()
    scale_size = models.IntegerField()

    class Meta:
        unique_together = ["manufacturer", "model_name"]
