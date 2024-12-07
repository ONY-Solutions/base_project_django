from rest_framework.response import Response
from rest_framework import status
from functools import wraps

def handle_view_errors():
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(view, *args, **kwargs):
            try:
                return view_func(view, *args, **kwargs)
            except Exception as e:
                return Response(e.args, status=status.HTTP_400_BAD_REQUEST)
        return wrapper
    return decorator