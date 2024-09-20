from django.db import models


class Vacancy(models.Model):
    company = models.CharField(max_length=255, null=False, blank=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField()
