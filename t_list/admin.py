import datetime

from django.contrib import admin

from t_list.models import Ezhednevnik


@admin.action(description="Завершить")
def deactivate(modeladmin, request, queryset):
    queryset.update(active_switch=False)
    queryset.update(status="Задача завершена")
    queryset.update(time_zav=datetime.datetime.now())


@admin.register(Ezhednevnik)
class EzhednevnikAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "zadachi",
        "time_nach",
        "active_switch",
        "status",
        "time_zav",
    ]
    list_filter = ["zadachi", "time_nach"]
    actions = [deactivate]
    search_fields = ("zadachi", "time_nach")


# Register your models here.
