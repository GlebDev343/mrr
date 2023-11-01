from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(unique=True)
    contact_details = models.CharField()
