from django.db import models
from django.conf import settings
from django.utils.timezone import now

from applications.company.models import Company


class UserLocation(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='locations'
    )
    latitude = models.FloatField()  # Широта
    longitude = models.FloatField()  # Долгота
    timestamp = models.DateTimeField(default=now)
    company = models.ForeignKey(Company, on_delete=models.CASCADE,
                                verbose_name='Company', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - ({self.latitude}, {self.longitude})"
