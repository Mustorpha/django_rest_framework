from django.db import models
from django.conf import settings
from django.db.models import Q

import random

User = settings.AUTH_USER_MODEL

TAGS_MODEL_VALUES = ['electronics', 'cars', 'movies', 'cameras']

class ProductQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)
    
    def search(self, query, user=None):
        lookup = Q(title__icontains=query) | Q(content__icontains=query)
        qs = self.is_public().filter(lookup)
        if user is not None:
            qs = qs.filter(user=user)
        return qs

class ProductManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return ProductQuerySet(self.model, using=self._db)

    def search(self, query, user=None):
        return self.get_queryset().search(query, user=user)

class Product(models.Model):
    user = models.ForeignKey(User, default=2, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length = 120)
    content = models.TextField(blank = True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=00.00)
    public = models.BooleanField(default=True)
    objects = ProductManager()

    @property
    def sale_price(self):
        return f'{float(self.price) * 0.8:.1f}'

    def is_public(self) -> bool:
        return self.public

    def get_tag_list(self):
        return [random.choice(TAGS_MODEL_VALUES)]