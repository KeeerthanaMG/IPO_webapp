from rest_framework import viewsets
from ipo.models import IPO
from ipo.serializers import IPOSerializer

class IPOViewSet(viewsets.ModelViewSet):
    queryset = IPO.objects.all()
    serializer_class = IPOSerializer
