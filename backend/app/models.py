from django.db import models
from django.contrib.auth.models import User


class Picture(models.Model):
    picture = models.ImageField("Картинка")
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="pictures",
        verbose_name="Пользователь",
    )
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.owner} - {self.picture}"

    class Meta:
        verbose_name = "Картинка"
        verbose_name_plural = "Картинки"
