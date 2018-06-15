from django.db import models

from common.models import BaseModel


class Book(BaseModel):
    name = models.CharField('book name', max_length=200)
    price = models.DecimalField('book price', max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    def dict(self):
        return {
            'id': self.pk,
            'name': self.name,
            'price': self.price
        }
