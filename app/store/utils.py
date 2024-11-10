from rest_framework import viewsets
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
import traceback
from .models import Historic

class ViewSetCustom(viewsets.ViewSet):
    
    def register_historic(self, title, activity):
        try:
            historic = Historic.objects.create(title=title, activity=activity)
        except Exception as e:
            return self.handle_exception(e, request)
    
    def check_permission(self, user, field, created_id=None):
        return True
    
    def handle_exception(self, e, request):
        if settings.DEBUG:
            traceback.print_exc()
            save_traceback = traceback.format_exc()
            return Response({'error': str(save_traceback)}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
