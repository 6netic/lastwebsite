from django.db import models


class Realisation(models.Model):
    """ Fields for table 'realisation' in mainsite """
    name = models.CharField(max_length=40, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    techno = models.CharField(max_length=20, blank=False)
    url = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return f"{self.name}"
