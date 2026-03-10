from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from .models import Airport, Booking

def home_view(request):
    return render(request, 'booking/home.html')

@login_required(login_url='login')
def booking_view(request):
    if request.user.is_staff:
        return redirect('staff_dashboard')
    
    airports = Airport.objects.all()
    
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        vehicle_name = request.POST.get('vehicle_name')
        license_plate = request.POST.get('license_plate')

        arrival_date = request.POST.get('arrival_date')
        pickup_date = request.POST.get('pickup_date')
        arrival_time = request.POST.get('time') 
        
        service_type = request.POST.get('service')
        airport_id = request.POST.get('airport')
        airport = get_object_or_404(Airport, id=airport_id)
        
        if not all([arrival_date, pickup_date, arrival_time, license_plate, service_type]):
            return render(request, 'booking/booking.html', {
            'airports': airports,
            'error': 'Please fill all required fields.'
            })

        # Create the booking
        booking = Booking.objects.create(
        user=request.user,
        customer_name=customer_name,
        vehicle_name=vehicle_name,
        license_plate=license_plate,
        arrival_date=arrival_date,
        pickup_date=pickup_date,
        time=arrival_time,
        service_type=service_type,
        airport=airport,
        status='pending')
        return redirect('dashboard', booking_id=booking.id)
        
    return render(request, 'booking/booking.html', {'airports': airports})

@login_required(login_url='login')
def dashboard_view(request, booking_id=None):
    
    if booking_id:
        booking = get_object_or_404(Booking, id=booking_id)
        if booking.user != request.user and not request.user.is_staff:
            return redirect('home')
            
        return render(request, 'booking/dashboard.html', {'booking': booking})
    
    bookings = Booking.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'booking/dashboard.html', {'bookings': bookings, 'is_list': True})

@staff_member_required
def staff_dashboard(request):
    bookings = Booking.objects.all().order_by('-created_at')
    status_choices = Booking.STATUS_CHOICES
    return render(request, 'booking/staff_dashboard.html', {
        'bookings': bookings,
        'status_choices': status_choices
    })

@staff_member_required
def update_booking_status(request, booking_id):
    if request.method == 'POST':
        booking = get_object_or_404(Booking, id=booking_id)
        new_status = request.POST.get('status')
        if new_status in dict(Booking.STATUS_CHOICES):
            booking.status = new_status
            booking.save()
    return redirect('staff_dashboard')
