from datetime import datetime
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


class Meter(models.Model):
    number = models.IntegerField()
    meter_model = models.ForeignKey(MeterModel, on_delete=models.CASCADE)
    manufacturer_date = models.DateField()

    class Meta:
        unique_together = ["number", "meter_model", "manufacturer_date"]


class PersonalAccount(models.Model):
    address = models.CharField()
    account_number = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(null=True, blank=True)
    phone_number = models.IntegerField(null=True)
    verification_code = models.CharField()
    code_validity = models.DateTimeField(default=datetime(2000, 1, 1, 0, 0))
