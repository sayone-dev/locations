from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from django_filters import rest_framework as filters

from location.serializers import LocationSerializer, LocationFilter
from location.models import Location


class LocationViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows locations to be viewed or edited.
	"""
	http_method_names = ['get', 'post', 'head']
	queryset = Location.objects.all().order_by('-created')
	serializer_class = LocationSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filter_class = LocationFilter
	permission_classes = (IsAuthenticated,)

