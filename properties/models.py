from django.db import models


class Property(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    street_address = models.CharField(max_length=200, null=False, blank=False)
    city = models.CharField(max_length=100, null=False, blank=False)
    # lol canada by default??
    province = models.CharField(max_length=100, null=False, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} in {self.city}, {self.province}"