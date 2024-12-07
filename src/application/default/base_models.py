from django.db import models
from django.conf import settings
from django.db.models.signals import post_save

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
    
    @classmethod
    def bulk_create_update_with_signals(cls, instances, fields=None):
        if fields is None:
            cls.objects.bulk_create(instances)
        else:
            cls.objects.bulk_update(instances,fields)

        for instance in instances:
            post_save.send(sender=cls, instance=instance, created= True if fields is None else False)

    class Meta:
        abstract = True
        ordering = ['id']
