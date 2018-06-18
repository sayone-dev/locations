from django.db import models
from django.contrib.auth.models import User


class Location(models.Model):
	user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
	name = models.CharField(max_length=250)
	latitude = models.DecimalField("Latitude", max_digits=30, decimal_places=15)
	longitude = models.DecimalField("Longitude", max_digits=30, decimal_places=15)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '%s' % (self.name)
