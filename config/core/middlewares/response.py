from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse
import json
import re
import logging


class CustomResponseMiddleware(MiddlewareMixin):
    def process_response(self, request, response):

        if 'application/json' in response['Content-Type']:
            try:
                data = json.loads(response.content)
            except json.JSONDecodeError:
                data = {}

            errors = data.get('errors', None)
            
            custom_response = {
                'status': response.status_code,
                'errors': errors,
                'data': data.get('data', None),  
                'method': request.method,
                'url': request.get_full_path()
            }

            return JsonResponse(custom_response, status=response.status_code)

        return response
