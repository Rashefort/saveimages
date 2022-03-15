from django.utils import timezone
from django.db import models


class User(models.Model):
    ip = models.GenericIPAddressField()
    url = models.CharField(max_length=128)
    comment = models.CharField(max_length=64, default='Комментарий отсутствует')
    date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.ip


    class Meta:
        ordering = ['-date']
