from rest_framework import routers


from . import viewsets


router = routers.DefaultRouter()
router.register(r'notes', viewsets.NoteModelViewSet)
urlpatterns = router.urls
