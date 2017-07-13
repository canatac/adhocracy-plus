from autoslug import AutoSlugField
from django.conf import settings
from django.db import models


class Organisation(models.Model):
    slug = AutoSlugField(populate_from='name', unique=True)
    name = models.CharField(max_length=512)
    initiators = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
    )

    def __str__(self):
        return self.name

    def has_initiator(self, user):
        return self.initiators.filter(id=user.id).exists()

    def get_absolute_url(self):
        # FIXME: not available yet
        return '#'
