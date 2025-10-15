from django.db import models

from core import constants

class Base(models.Model):
    created_at = models.DateTimeField(
        "Criado em",
        auto_now_add=True,
        null=True
    )
    modified_at = models.DateTimeField(
        "Atualizado em",
        auto_now=True,
        null=True
    )
    status = models.BooleanField(
        choices=constants.STATUS,
        default=constants.ATIVO
    )

    class Meta:
        abstract = True
