@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    # Make sure these names are EXACTLY what you wrote in models.py
    list_display = ('patient_name', 'phone_number', 'appointment_date', 'created_at') 
    list_filter = ('appointment_date', 'created_at')
    search_fields = ('patient_name', 'phone_number')
    ordering = ('-appointment_date', '-created_at')
    readonly_fields = ('created_at',)
    
    fieldsets = (
        ('Patient Details', {
            'fields': ('patient_name', 'phone_number')
        }),
        ('Schedule Information', {
            'fields': ('appointment_date',)
        }),
    )