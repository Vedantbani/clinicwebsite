from django.contrib import admin
from .models import Appointment  # Replace with your actual Appointment model name if different

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    # 1. Choose which columns are visible in the main table layout list
    list_display = ('name', 'phone', 'appointment_date', 'created_at')
    
    # 2. Add an interactive right-hand sidebar filter panel
    list_filter = ('appointment_date', 'created_at')
    
    # 3. Add a live search bar at the top to find patients quickly by name or phone
    search_fields = ('name', 'phone')
    
    # 4. Sort the appointments so the newest bookings appear right at the top
    ordering = ('-appointment_date', '-created_at')
    
    # 5. Make the data layout display read-only or cleanly organized
    readonly_fields = ('created_at',)
    
    # Optional: Break the appointment detail page into neat visual groups
    fieldsets = (
        ('Patient Details', {
            'fields': ('name', 'phone')
        }),
        ('Schedule Information', {
            'fields': ('appointment_date',)
        }),
        ('System Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',), # Minimizes this section by default
        }),
    )

# Customizing the overall Admin Portal Branding titles
admin.site.site_header = "SSNC Administration Portal"
admin.site.site_title = "SSNC Admin Control"
admin.site.index_title = "Welcome to Shree Sahaj Naturopathy Clinic Management"