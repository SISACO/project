from django import forms
from .models import Alumni, ProfessionalInfo, EducationInfo, CareerPath, AlumniInvolvement, CommunicationPreferences, NetworkingPreferences, SocialMediaLinks

class AlumniForm(forms.ModelForm):
    class Meta:
        model = Alumni
        fields = ['full_name', 'graduation_year', 'contact_email']

class ProfessionalInfoForm(forms.ModelForm):
    class Meta:
        model = ProfessionalInfo
        fields = ['job_title', 'company', 'industry']

class EducationInfoForm(forms.ModelForm):
    class Meta:
        model = EducationInfo
        fields = ['major']

class CareerPathForm(forms.ModelForm):
    class Meta:
        model = CareerPath
        fields = ['career_trajectory']

class AlumniInvolvementForm(forms.ModelForm):
    class Meta:
        model = AlumniInvolvement
        fields = ['events_attended']

class CommunicationPreferencesForm(forms.ModelForm):
    class Meta:
        model = CommunicationPreferences
        fields = ['newsletter_opt_in']

class NetworkingPreferencesForm(forms.ModelForm):
    class Meta:
        model = NetworkingPreferences
        fields = ['mentoring_interest']

class SocialMediaLinksForm(forms.ModelForm):
    class Meta:
        model = SocialMediaLinks
        fields = ['linkedin_profile']
