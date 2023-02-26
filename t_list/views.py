import datetime
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)


from django.http import HttpResponse
from django.urls import reverse_lazy

from rest_framework import viewsets, mixins
from t_list.models import Ezhednevnik
from .serializers import ZadachiSerializer
from .filters import ZadachiFilterSet


def current_datetime(request):
    now = datetime.datetime.now()
    html = f"Now {now}"
    return HttpResponse(html)


class ZadachaListView(ListView):
    model = Ezhednevnik
    context_object_name = "zadachis"
    template_name = "z_list.html"


class ZadachaCreateView(CreateView):
    model = Ezhednevnik
    fields = ["zadachi"]
    template_name = "z_create.html"
    success_url = "/data/"


class ZadachaUpdateView(UpdateView):
    model = Ezhednevnik
    fields = ["zadachi", "active_switch", "status"]
    template_name = "z_u_detail.html"
    success_url = "/data/"


class ZadachaDeleteView(DeleteView):
    model = Ezhednevnik
    context_object_name = "zadachi"
    success_url = reverse_lazy("Ezhednevnik")
    template_name = "z_del.html"
    success_url = "/data/"


class ZadachaViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Ezhednevnik.objects.all().order_by("id")
    serializer_class = ZadachiSerializer
    filterset_class = ZadachiFilterSet

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
