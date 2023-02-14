from django.db.models import Count, Sum, Manager

# https://docs.djangoproject.com/en/4.1/topics/db/aggregation/
# https://django.fun/ru/docs/django/4.1/topics/db/aggregation/
from django.db.models import QuerySet


# class AnnotatedManager(Manager):
#     def get_queryset(self) -> QuerySet:
#         """Переопределение метода get_queryset.
#
#         Метод будет вызываться при каждой выборке из таблицы.
#         """
#         qs = super().get_queryset()
#         # заполучить исходный QuerySet, как будто его еще не переопределили.
#
#         qs = qs.prefetch_related("zadachi")
#         # prefetch_related - в одном запросе сджойнит и выгрузит все связанные с корзиной товары
#         # тем самым уберет необходимость по каждой корзине ходить за связанными товарами чем снизит нагрузку на базу
#         # https://django.fun/ru/docs/django/4.1/ref/models/querysets/#prefetch-related
#
#         qs = qs.annotate(amount=Count("zadachi"))
#         # По полю amount можно получить количество товаров в корзине
#
#         qs = qs.annotate(total_sum=Sum("zadachi"))
#         # По полю total_sum можно получить количество сумму цен товаров в корзине
#
#         return qs
