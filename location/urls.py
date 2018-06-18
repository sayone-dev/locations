from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

from location import views

router = routers.DefaultRouter()
router.register(r'locations', views.LocationViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
	url(r'^api-token-auth/', obtain_jwt_token),
]
