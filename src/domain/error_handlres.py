from django.db.utils import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
class ErrorHandler:
    
    @staticmethod
    def handle_error(exception, model):
        
        def integrityErrors(exception):
            if type(exception.args) == tuple:
                if 'foreign key constraint' in str(exception.args[0]):
                    return {"error": "Integrity Error.", "details": f"{model} with that id don't exist"}
            return {"error": "Integrity error.", "details": f"A {model} with this data already exists or violates integrity constraints."}
            
        if isinstance(exception, ObjectDoesNotExist):
            return {"error": "Invalid data.", "details": str(exception)}
        elif isinstance(exception, IntegrityError):
            return integrityErrors(exception)
        elif isinstance(exception, KeyError):
            return {"error": f"{model} Error", "details": str(exception)}
        elif isinstance(exception, ValueError):
            return {"error": "Invalid data.", "details": str(exception)}
        else:
            return {"error": "An unexpected error occurred.", "details": str(exception)}
