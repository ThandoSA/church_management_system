from django.urls import path

urlpatterns = [
    path('members/', include('members.urls')),  # URL patterns for members
    path('staff/', include('staff.urls')),      # URL patterns for staff
    path('events/', include('events.urls')),    # URL patterns for events
    path('announcements/', include('announcements.urls')),  # URL patterns for announcements
    path('donations/', include('donations.urls')), # URL patterns for donations
    path('attendance/', include('attendance.urls')), # URL patterns for attendance
]