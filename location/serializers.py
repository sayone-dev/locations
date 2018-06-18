from django.contrib.auth.models import User

from rest_framework import serializers
from django_filters import DateRangeFilter, DateFilter, FilterSet
from django_filters.widgets import RangeWidget
from django_filters import rest_framework as filters
from location.models import Location


class LocationFilter(filters.FilterSet):
    created = filters.DateFromToRangeFilter(name='created', widget=RangeWidget(attrs={'placeholder': 'MM/DD/YYYY'}))

    class Meta:
        model = Location
        fields = ['created',]


class LocationSerializer(serializers.HyperlinkedModelSerializer):
	user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), default=serializers.CurrentUserDefault())

	class Meta:
		model = Location
		fields = ('user', 'name', 'latitude', 'longitude')
		
		
