from django import forms
from .models import UserProfile, ElectiveSubject

class UserProfileForm(forms.ModelForm):
    elective_subjects = forms.ModelMultipleChoiceField(
        queryset=ElectiveSubject.objects.all(), 
        widget=forms.CheckboxSelectMultiple, 
        required =True
    )

    class Meta:
        model = UserProfile
        fields = ['name', 'email', 'elective_subjects', 'aggregate', 'career_aspiration']