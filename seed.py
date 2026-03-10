from django.contrib.auth.models import User
from booking.models import ParkingZone

# Create superuser
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')

# Create parking zones
zones = [
    {'name': 'Terminal A - Deck 1', 'deck': 'A1'},
    {'name': 'Terminal A - Deck 2', 'deck': 'A2'},
    {'name': 'Terminal B - Premium', 'deck': 'B1'},
    {'name': 'Valet Zone', 'deck': 'V1'}
]

for zone in zones:
    ParkingZone.objects.get_or_create(name=zone['name'], deck=zone['deck'])
    
print("Successfully seeded database with admin user and parking zones.")
