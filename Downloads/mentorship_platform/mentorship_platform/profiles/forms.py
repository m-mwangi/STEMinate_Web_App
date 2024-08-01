from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'expertise', 'goals', 'mentorship_preferences', 'availability', 'preferred_communication_methods')
