from rest_framework.routers import DefaultRouter
from t_list.views import ZadachaViewSet

# router = DefaultRouter(trailing_slash=False)
router = DefaultRouter()

app_name = "t_listapp"


router.register(
    prefix="zadachis",
    viewset=ZadachaViewSet,
    basename="zadachis",
)

urlpatterns = router.urls