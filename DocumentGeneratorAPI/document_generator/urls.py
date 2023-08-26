from rest_framework.routers import DefaultRouter
from .views import GenerateDocumentViewSet

router = DefaultRouter()
router.register(r'', GenerateDocumentViewSet)
urlpatterns = router.urls
