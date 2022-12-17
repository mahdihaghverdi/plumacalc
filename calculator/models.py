from django.db import models


class History(models.Model):
    input = models.CharField(max_length=250)
    answer = models.CharField(max_length=250, null=True)
    errors = models.CharField(max_length=250, null=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.errors is None:
            return f"{self.input} = {self.answer}"
        return f'{self.input} had {self.errors!r} error!'
