from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from booking.views import home_view, booking_view, dashboard_view, staff_dashboard, update_booking_status
from booking.auth_views import register_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('book/', booking_view, name='book'),
    path('dashboard/', dashboard_view, name='dashboard_latest'),
    path('dashboard/<int:booking_id>/', dashboard_view, name='dashboard'),
    path('register/', register_view, name='register'),
    path('staff/', staff_dashboard, name='staff_dashboard'),
    path('staff/update/<int:booking_id>/', update_booking_status, name='update_booking_status'),
    path('login/', LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
