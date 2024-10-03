from django.contrib.auth.models import User
from django_filters import FilterSet, NumberFilter, CharFilter

from apps.models import Product


class ProductFilter(FilterSet):
    description = CharFilter(lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['name', 'category', 'owner', 'description']


# users/?first_name=Islom&last_name=&min_price=2&max_price=3