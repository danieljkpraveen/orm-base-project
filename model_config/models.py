from django.db import models
from manage import base_django
base_django()


class TestModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    