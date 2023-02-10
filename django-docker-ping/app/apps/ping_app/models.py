from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Ping(models.Model):
    host = models.CharField(_("host"), max_length=50)
    created_at = models.DateTimeField(_("datetime"), auto_now_add=True)
