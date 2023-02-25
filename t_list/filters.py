from django_filters import rest_framework as dj_filters
from .models import Ezhednevnik


class ZadachiFilterSet(dj_filters.FilterSet):
    """Набор фильров для представления для модели статей."""

    zadachi = dj_filters.CharFilter(field_name="zadachi", lookup_expr="icontains")

    order_by_field = "ordering"

    class Meta:
        model = Ezhednevnik
        fields = [
            "zadachi",
        ]
