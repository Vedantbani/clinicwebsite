from django.contrib import admin
from .models import Appointment  # Replace with your actual model name if it's different

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'appointment_date', 'created_at') # Ensure these match your models.py fields!
    list_filter = ('appointment_date', 'created_at')
    search_fields = ('name', 'phone')
    ordering = ('-appointment_date', '-created_at')
    readonly_fields = ('created_at',)
    
    fieldsets = (
        ('Patient Details', {
            'fields': ('name', 'phone')
        }),
        ('Schedule Information', {
            'fields': ('appointment_date',)
        }),
    )

# Admin Branding Customizations
admin.site.site_header = "SSNC Administration Portal"
admin.site.site_title = "SSNC Admin Control"
admin.site.index_title = "Welcome to Shree Sahaj Naturopathy Clinic Management"