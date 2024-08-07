from django.db.utils import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
class ErrorHandler:
    @staticmethod
    def handle_error(exception, model):

        if isinstance(exception, IntegrityError):
            return {"error": "Integrity error.", "details": f"A {model} with this data already exists or violates integrity constraints."}
        elif isinstance(exception, KeyError):
            return {"error": f"{model} not found.", "details": str(exception)}
        elif isinstance(exception, ValueError):
            return {"error": "Invalid data.", "details": str(exception)}
        elif isinstance(exception, ObjectDoesNotExist):
            return {"error": "Invalid data.", "details": str(exception)}
        else:
            return {"error": "An unexpected error occurred.", "details": str(exception)}
