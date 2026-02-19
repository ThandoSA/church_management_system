# church_management_system
Church Management System with Calendar, Staff, Members, Donations

Project Structure
church_management/
├── church_management/       # Project settings
├── church/                  # Main app
│   ├── models.py           # Database models
│   ├── views.py            # Views and logic
│   ├── forms.py            # Django forms
│   ├── urls.py             # URL routing
│   ├── admin.py            # Admin configuration
│   ├── templates/          # HTML templates
│   └── static/             # CSS, JS, images
├── manage.py               # Django management
└── requirements.txt        # Dependencies

Models
Core Models
ChurchInfo - Church organization details
Member - Church members database
StaffRole - Staff position definitions
Staff - Staff member records
ChurchCalendar - Events and calendar
Attendance - Member attendance records
Donation - Financial donations
Announcement - Church announcements
ServiceSchedule - Recurring services
StaffSchedule - Staff work schedules
Usage
Adding Members
Navigate to Members → Add Member
Fill in member details
Save
Managing Events
Go to Events → Create Event
Set event date, time, location
Assign organizer (optional)
Save
Recording Donations
Go to Finances
Click "Record Donation"
Enter donation details
Save
Creating Announcements
Navigate to Announcements → New Announcement
Enter title and content
Upload image (optional)
Pin if important
Save
Admin Panel
Access the admin panel at /admin/ to:

Manage all models
Create staff roles
Configure service schedules
View analytics
Technologies Used
Backend: Django 4.2.8
Database: SQLite3
Frontend: Bootstrap 5, HTML5, CSS3, JavaScript
Forms: Django Crispy Forms with Bootstrap 5
Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Support
For support, please open an issue on the GitHub repository.

