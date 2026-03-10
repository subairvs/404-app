from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Airport(models.Model):
    name = models.CharField(max_length=100)
    location_code = models.CharField(max_length=10) 

    def __str__(self):
        return f"{self.name} ({self.location_code})"

class Booking(models.Model):
    SERVICE_CHOICES = [
        ('parking', 'Secure Airport Parking (₹899/starting)'),
        ('wash', 'Signature Premium Wash (₹1899/starting)'),
        ('coating', 'Advanced Ceramic Coating (₹17999/starting)'),
    ]

    STATUS_CHOICES = [
        ('pending',             'Booking Confirmed'),
        ('received',            'Vehicle Received'),
        ('in-progress-wash',    'In Progress'),
        ('in-progress-coating', 'Service Completing'),
        ('done',                'Done'),
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    customer_name = models.CharField(max_length=100)
    vehicle_name = models.CharField(max_length=50,default="Unknown")
    license_plate = models.CharField(max_length=20)
    
    pickup_date = models.DateField(null=True, blank=True)
    arrival_date = models.DateField(null=True, blank=True)
    time = models.TimeField()
    
    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES, default='wash')
    airport = models.ForeignKey(Airport, on_delete=models.SET_NULL, null=True)
    
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.vehicle_name} ({self.get_status_display()})"
