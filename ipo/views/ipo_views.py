from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from ipo.models import IPO
from ipo.serializers import IPOSerializer

class IPOViewSet(viewsets.ModelViewSet):
    queryset = IPO.objects.all()
    serializer_class = IPOSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['status', 'company']  # enable filter by ?status=Open
    ordering_fields = ['listing_date', 'ipo_price', 'current_return']
