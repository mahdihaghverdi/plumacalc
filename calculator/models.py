from django.db import models


class History(models.Model):
    input = models.CharField(max_length=250)
    answer = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.input} = {self.answer}"
