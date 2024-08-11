from django.db.utils import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
class ErrorHandler:
    @staticmethod
    def handle_error(exception, model):

        print(exception)
        
        if isinstance(exception, ObjectDoesNotExist):
            return {"error": "Invalid data.", "details": str(exception), "status": 404}
        elif isinstance(exception, IntegrityError):
            return {"error": "Integrity error.", "details": f"A {model} with this data already exists or violates integrity constraints.", "status": 400}
        elif isinstance(exception, KeyError):
            return {"error": f"{model} Error", "details": str(exception), "status": 400}
        elif isinstance(exception, ValueError):
            return {"error": "Invalid data.", "details": str(exception), "status": 400}
        else:
            return {"error": "An unexpected error occurred.", "details": str(exception), "status": 500}
