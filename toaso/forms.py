from django import forms
from .models import UserProfile, ElectiveSubject, Interest

class UserProfileForm(forms.ModelForm):
    elective_subjects = forms.ModelMultipleChoiceField(
        queryset=ElectiveSubject.objects.all(), 
        widget=forms.CheckboxSelectMultiple, 
        required =True
    )
    interests = forms.ModelChoiceField(
        queryset=Interest.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = UserProfile
        fields = ['name', 'email', 'elective_subjects', 'aggregate', 'career_aspiration', 'interests']