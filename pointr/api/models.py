from django.db import models
from django.utils.translation import gettext as _


class Points(models.Model):
    points_list = models.TextField()
    closest_points = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = _("Points")
        verbose_name_plural = _("Points")

    def __str__(self) -> str:
        return self.points_list
