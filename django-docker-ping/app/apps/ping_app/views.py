import time
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.conf import settings
from apps.ping_app.serializers import PingSerializer, IncomePingSerializer
from apps.ping_app.models import Ping

# Create your views here.
class PingView(APIView):
    parser_classes = (JSONParser,)
    serializer_class = IncomePingSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        """ Create an order """
        serializer = IncomePingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        Ping(
            host=request.META.get('REMOTE_ADDR')
        ).save()
        
        data = {
            'address': request.META.get('REMOTE_ADDR'),
            'count': request.data['count']
        }

        return Response(status=200, data=data)
