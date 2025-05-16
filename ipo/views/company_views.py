# views/company_views.py
from rest_framework import viewsets
from ipo.models import Company
from ipo.serializers import CompanySerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
