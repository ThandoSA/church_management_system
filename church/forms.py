from django import forms

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member  # Make sure to replace with the actual Member model
        fields = '__all__'

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff  # Replace with the actual Staff model
        fields = '__all__'

class EventForm(forms.ModelForm):
    class Meta:
        model = Event  # Replace with actual Event model
        fields = '__all__'

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement  # Replace with actual Announcement model
        fields = '__all__'

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation  # Replace with actual Donation model
        fields = '__all__'