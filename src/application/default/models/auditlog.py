from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

class AuditLog(models.Model):
    TABLE_OPERATIONS = (
        ('INSERT', 'Insert'),
        ('UPDATE', 'Update'),
        ('DELETE', 'Delete')
    )

    table_name = models.CharField(max_length=100)
    operation = models.CharField(max_length=10, choices=TABLE_OPERATIONS)
    row_id = models.IntegerField(null=True)
    old_data = models.JSONField(null=True)
    new_data = models.JSONField(null=True)
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True
    )
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['table_name', 'row_id']),
            models.Index(fields=['timestamp']),
        ]
