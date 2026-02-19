Church Management System

A full-stack Church Management System built with Django to manage members, staff, events, donations, attendance, and internal communication from a centralized platform.

This system is designed to streamline administrative operations, improve record keeping, and enhance organizational efficiency within a church environment.

🚀 Features

Member Management

Staff & Role Management

Church Calendar & Events

Attendance Tracking

Donation Recording

Announcements System

Service & Staff Scheduling

Admin Dashboard

Analytics (via Django Admin)

🏗 Project Structure
church_management/
├── church_management/       # Project settings
├── church/                  # Main application
│   ├── models.py           # Database models
│   ├── views.py            # Business logic
│   ├── forms.py            # Django forms
│   ├── urls.py             # URL routing
│   ├── admin.py            # Admin configuration
│   ├── templates/          # HTML templates
│   └── static/             # CSS, JS, images
├── manage.py               # Django CLI management
└── requirements.txt        # Dependencies


🗄 Database Models
Core Models

ChurchInfo – Church organization details

Member – Church members database

StaffRole – Staff position definitions

Staff – Staff member records

ChurchCalendar – Events and calendar entries

Attendance – Member attendance records

Donation – Financial donations tracking

Announcement – Church announcements

ServiceSchedule – Recurring services

StaffSchedule – Staff work schedules

