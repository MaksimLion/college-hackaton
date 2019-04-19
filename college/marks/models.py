from django.db import models
from authentication.models import Profile, Subject


class Mark(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    mark = models.CharField(max_length=2)
    half_year = models.CharField()

    class Meta:
        verbose_name = "Оценка"
        verbose_name_plural = "Оценки"
