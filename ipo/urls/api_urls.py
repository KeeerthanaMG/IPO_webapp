from django.urls import path
from rest_framework.routers import DefaultRouter

from ipo.views.company_views import CompanyViewSet
from ipo.views.ipo_views import IPOViewSet
from ipo.views.document_views import DocumentViewSet

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'ipos', IPOViewSet)
router.register(r'documents', DocumentViewSet)

urlpatterns = router.urls
