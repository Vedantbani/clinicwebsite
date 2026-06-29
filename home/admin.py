from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    # 1. Dynamically grab all model fields
    all_fields = [field.name for field in Appointment._meta.fields]
    list_display = all_fields
    
    # 2. Make the very first column (usually ID or Name) a clickable link to open details
    list_display_links = (all_fields[0],) 
    
    # 3. Simple live search
    search_fields = ('name', 'phone')

    # 4. Custom trick to rename Django's default column headers or text to be simpler
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Replaces internal technical strings to make management highly readable
        self.list_display_links = [f for f in self.list_display if f in ['name', 'id', all_fields[0]]]

# Admin Interface Branding
admin.site.site_header = "SSNC Administration Portal"
admin.site.site_title = "SSNC Admin Control"
admin.site.index_title = "Patient Bookings Dashboard"