import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from django.contrib.auth.models import User
from booking.models import Airport

# Create admin user
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')

# Create airports
airports = [
    {"name": "Indira Gandhi International Airport", "location_code": "DEL"},
    {"name": "Chhatrapati Shivaji Maharaj International Airport", "location_code": "BOM"},
    {"name": "Kempegowda International Airport", "location_code": "BLR"},
    {"name": "Cochin International Airport", "location_code": "COK"},
]

for airport in airports:
    Airport.objects.get_or_create(**airport)

print("Database seeded successfully.")