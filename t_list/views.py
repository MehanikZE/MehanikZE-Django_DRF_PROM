import datetime
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)
from t_list.models import Ezhednevnik
from django.http import HttpResponse
from django.urls import reverse_lazy


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