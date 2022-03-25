from django.db import models
from sortedm2m.fields import SortedManyToManyField
from properties.models import Property


class Landlord(models.Model):
    """
    Unfortunately I'm not adding support for the Ricky Bobbys of the world.
    Those with multiple middle(?) names will simply need to deal with the reality
    that their parents failed them. Sad but true story. @Swordoflighting
    """
    first_name = models.CharField(max_length=72, null=False, blank=False)
    # Middle name being optional here.
    middle_name = models.CharField(max_length=72, null=True, blank=True)
    last_name = models.CharField(max_length=72, null=False, blank=False)
    properties = SortedManyToManyField(Property)

    # TODO: Make sure that `SortedManyToManyField` is actually iterable out of the box, I don't think it is.
    def __str__(self):
        return f"{self.first_name} {self.last_name} Property Count [{len(self.properties)}]"