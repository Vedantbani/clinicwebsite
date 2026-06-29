from django.db import models

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    preferred_date = models.DateField()
    therapy_or_package = models.CharField(max_length=100)
    health_notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically tracks when they booked

    def __str__(self):
        return f"{self.name} - {self.therapy_or_package} on {self.preferred_date}"