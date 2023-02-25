from django.db import models


class Ezhednevnik(models.Model):
    zadachi = models.CharField(max_length=150, help_text="Название задачи")
    time_nach = models.DateTimeField(auto_now=True, help_text="Время начала")
    active_switch = models.BooleanField(
        default=True,
        help_text="Статус задачи, снять галочку для завершения, установить для продолжения работ",
    )
    status = models.CharField(
        max_length=150,
        help_text="Статус задачи, комментарий к завершению",
        default="В работе",
    )
    time_zav = models.DateTimeField(auto_now=True, help_text="Время завершения")

    def __str__(self):
        return f"Ezhednevnik {self.id}|{self.zadachi}|{self.time_nach}|{self.active_switch}|{self.status}"


# Create your models here.
