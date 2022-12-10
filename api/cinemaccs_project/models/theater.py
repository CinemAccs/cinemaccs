from django.db import models

class Theater(models.Model):
    company_name = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=300, null=True)
    internal_id = models.CharField(max_length=10, null=True)
    complexSlug = models.CharField(max_length=100, null=True)
    cinemaNationalId = models.IntegerField(null=True)
    address1 = models.CharField(max_length=300, null=True)
    address2 = models.CharField(max_length=300, null=True)
    city = models.CharField(max_length=100, null=True)
    zipcode = models.IntegerField(null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    parkingInfo = models.CharField(max_length=300, null=True)
    isGiftStore = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=1000, null=True)
    accessibilityDescription = models.CharField(max_length=1000, null=True)
    publicTransport = models.CharField(max_length=300, null=True)
    currencyCode = models.CharField(max_length=100, null=True)
    allowPrintAtHomeBookings = models.CharField(max_length=10, null=True)
    allowOnlineVoucherValidation = models.CharField(max_length=10, null=True)
    displaySofaSeats = models.CharField(max_length=10, null=True)
    timeZoneId = models.CharField(max_length=100, null=True)
    createdDate = models.DateTimeField(auto_now_add=True, null=True)
    modifiedDate = models.DateTimeField(auto_now=True, null=True)
    