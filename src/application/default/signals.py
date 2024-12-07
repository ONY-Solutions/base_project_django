from django.db.models.signals import pre_save, post_save, pre_delete
from django.dispatch import receiver
from config.core.middlewares.auditLog import AuditMiddleware
from src.application.default.models.auditlog import AuditLog
import json
from src.interfaces.helpers.json_encoders import CustomJSONEncoder

def should_audit_model(model):
    """Determina si un modelo debe ser auditado"""
    return hasattr(model, 'audit_log') and model.audit_log

def get_model_fields(instance):
    """Obtiene los campos del modelo en formato JSON"""
    return {
        field.name: getattr(instance, field.name)
        for field in instance._meta.fields
        if not field.is_relation
    }

@receiver(pre_save)
def pre_save_handler(sender, instance, **kwargs):
    if not should_audit_model(sender):
        return
        
    if instance.pk:
        try:
            instance._original_state = sender.objects.get(pk=instance.pk)
        except sender.DoesNotExist:
            instance._original_state = None

@receiver(post_save)
def post_save_handler(sender, instance, created, **kwargs):
    if not should_audit_model(sender):
        return
    
    new_data = get_model_fields(instance)
    new_data = json.dumps(new_data, cls=CustomJSONEncoder)
    
    if created:
        AuditLog.objects.create(
            table_name=sender._meta.db_table,
            operation='INSERT',
            row_id=instance.pk,
            new_data=new_data,
            user=AuditMiddleware.get_current_user()
        )
    else:
        old_data = json.dumps(get_model_fields(instance._original_state) if hasattr(instance, '_original_state') else {}, cls=CustomJSONEncoder)
        if old_data != new_data:
            AuditLog.objects.create(
                table_name=sender._meta.db_table,
                operation='UPDATE',
                row_id=instance.pk,
                old_data=old_data,
                new_data=new_data,
                user=AuditMiddleware.get_current_user()
            )

@receiver(pre_delete)
def pre_delete_handler(sender, instance, **kwargs):
    if not should_audit_model(sender):
        return

    AuditLog.objects.create(
        table_name=sender._meta.db_table,
        operation='DELETE',
        row_id=instance.pk,
        old_data=json.dumps(get_model_fields(instance), cls=CustomJSONEncoder),
        user=AuditMiddleware.get_current_user()
    )