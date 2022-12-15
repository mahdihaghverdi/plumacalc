from django.db import models


class History(models.Model):
    input = models.CharField(max_length=250)
    answer = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.input} = {self.answer}"
