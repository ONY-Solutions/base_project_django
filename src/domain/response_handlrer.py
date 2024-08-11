import functools
from abc import ABCMeta
from src.domain.error_handlres import ErrorHandler
from django.db.transaction import atomic, rollback

def format_method(method):
    @functools.wraps(method)
    def wrapper(*args, **kwargs):
        try:
            with atomic():
                result = method(*args, **kwargs)
                return {"status": 200, "data": result}
        except Exception as e:
            rollback()
            response = ErrorHandler.handle_error(e,args[0].model)
            return {"status":response["status"], "error": response["details"]}
    return wrapper


class ServiceMeta(ABCMeta):
    def __new__(cls, name, bases, attrs):
        for attr_name, attr_value in attrs.items():
            if callable(attr_value) and not attr_name.startswith("__"):
                attrs[attr_name] = format_method(attr_value)
        return super().__new__(cls, name, bases, attrs)