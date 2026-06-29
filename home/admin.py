from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    # 1. Pull all your model's fields dynamically
    list_display = [field.name for field in Appointment._meta.fields]
    
    # 2. Make the first column (the ID) clickable to view details instantly
    list_display_links = (list_display[0],)
    
    # 3. Simple search configuration using name and phone
    search_fields = ('name', 'phone')

    # 4. Optional: If 'name' is an actual column in your table, let's make it clickable too!
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'name' in self.list_display:
            self.list_display_links = (self.list_display[0], 'name')
            
# Admin Interface Branding Titles
admin.site.site_header = "SSNC Administration Portal"
admin.site.site_title = "SSNC Admin Control"
admin.site.index_title = "Patient Bookings Dashboard"