from django.db import models


class History(models.Model):
    input = models.CharField(max_length=250)
