from django.db import models

from accounts.models import Base

class Cardbank(Base):
    name = models.CharField("Nome", max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Banco do cartão"
        verbose_name_plural = "Bancos do cartão"
        ordering = ["-id"]
        # db_table = 'website_cardbank'
