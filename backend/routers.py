from api.viewsets import NatureViewset, PaysViewset, RegionViewset, DocumentViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('nature', NatureViewset)
router.register('pays', PaysViewset)
router.register('region', RegionViewset)
router.register('document', DocumentViewset)
