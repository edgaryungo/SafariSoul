from django.contrib import admin
from .models import Customer, CulturalAttraction, Destination, TourPackage, Booking

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number', 'created_at', 'updated_at']

@admin.register(CulturalAttraction)
class CulturalAttractionAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created_at', 'updated_at']

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'cultural_attraction', 'created_at', 'updated_at']

@admin.register(TourPackage)
class TourPackageAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'destination', 'price', 'start_date', 'duration_days', 'duration_nights', 'created_at', 'updated_at']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['customer', 'tour_package', 'booking_date', 'num_of_people', 'created_at', 'updated_at']

