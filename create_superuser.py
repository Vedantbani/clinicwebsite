import os
import django

# Set up the Django environment configuration
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clinic.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Account credentials to create
USERNAME = 'vedantbani'
EMAIL = 'vedantbani1234@gmail.com'
PASSWORD = 'YourSecurePassword2026'  # Change this to your chosen password!

if not User.objects.filter(username=USERNAME).exists():
    print(f"Creating superuser account for {USERNAME}...")
    User.objects.create_superuser(USERNAME, EMAIL, PASSWORD)
    print("Superuser created successfully!")
else:
    # If the user exists, force update their password just in case it was wrong
    print(f"User {USERNAME} exists. Resetting password...")
    user = User.objects.get(username=USERNAME)
    user.set_password(PASSWORD)
    user.is_superuser = True
    user.is_staff = True
    user.save()
    print("Password updated successfully!")