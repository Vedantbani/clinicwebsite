from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'preferred_date', 'therapy_or_package', 'created_at')
    list_filter = ('preferred_date', 'therapy_or_package')
    search_fields = ('name', 'phone')