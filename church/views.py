from django.shortcuts import render
from django.http import HttpResponse

# View for the church dashboard
class DashboardView:
    def get(self, request):
        return HttpResponse('Dashboard')

# View for church members
class MembersView:
    def get(self, request):
        return HttpResponse('Members')

# View for church staff
class StaffView:
    def get(self, request):
        return HttpResponse('Staff')

# View for church events
class EventsView:
    def get(self, request):
        return HttpResponse('Events')

# View for announcements
class AnnouncementsView:
    def get(self, request):
        return HttpResponse('Announcements')

# View for donations
class DonationsView:
    def get(self, request):
        return HttpResponse('Donations')

# View for attendance
class AttendanceView:
    def get(self, request):
        return HttpResponse('Attendance')
