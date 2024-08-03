from django.db import models
from django.conf import settings

class BaseModel(models.Model):
    createdAt = models.DateField(auto_now_add=True, blank=True, null= True)
    updateAt = models.DateField(auto_now=True, blank=True, null=True)
    userCreate = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="+",
        db_index=True,
    )
    userUpdate = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="+",
        db_index=True,
    )
    visible = models.BooleanField(default=True)

    def __str__(self) -> str:
        return str(self.pk)

    class Meta:
        abstract = True
        ordering = ['id']
