from django.contrib import admin
from .models import Airport, Booking

@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    list_display = ('name', 'location_code')
    search_fields = ('name', 'location_code')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'vehicle_name', 'airport', 'service_type', 'status', 'created_at')
    list_editable = ('status',)

    list_filter = ('airport', 'status', 'service_type', 'pickup_date','arrival_date')
    search_fields = ('customer_name', 'vehicle_name', 'license_plate')