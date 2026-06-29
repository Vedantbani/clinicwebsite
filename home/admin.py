from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    # This automatically grabs EVERY field inside your model so it NEVER causes a crash!
    list_display = [field.name for field in Appointment._meta.fields]
    
    # Simple search configuration using name and phone
    # (If your model uses different names like 'patient_name', change them here)
    search_fields = ('name', 'phone') 

# Admin Branding Customizations
admin.site.site_header = "SSNC Administration Portal"
admin.site.site_title = "SSNC Admin Control"
admin.site.index_title = "Welcome to Shree Sahaj Naturopathy Clinic Management"