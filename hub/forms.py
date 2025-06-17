from django.forms import ModelForm
from .models import *
from django import forms
from .models import WorkshopRegistration, FestivalTicket
from .models import Profile
from django.contrib.auth.models import User
from .models import Artwork

class ArtworkForm(forms.ModelForm):
    class Meta:
        model = Artwork
        fields = ['title', 'description', 'image']

class WorkshopForm(forms.ModelForm):
    class Meta:
        model = WorkshopRegistration
        fields = ['name', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full border p-2 rounded', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'w-full border p-2 rounded', 'placeholder': 'Email Address'}),
        }

class FestivalForm(forms.ModelForm):
    class Meta:
        model = FestivalTicket
        fields = ['name', 'tickets']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full border p-2 rounded', 'placeholder': 'Your Name'}),
            'tickets': forms.NumberInput(attrs={'class': 'w-full border p-2 rounded', 'placeholder': 'Number of Tickets'}),
        }

# forms.py

class ProfileForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = Profile
        fields = ['profile_pic', 'bio']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ProfileForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['name'].initial = user.get_full_name()
            self.fields['email'].initial = user.email

    def save(self, commit=True):
        profile = super().save(commit=False)
        user = profile.user

        if 'name' in self.cleaned_data:
            name_parts = self.cleaned_data['name'].split(' ', 1)
            user.first_name = name_parts[0]
            user.last_name = name_parts[1] if len(name_parts) > 1 else ''
        if 'email' in self.cleaned_data:
            user.email = self.cleaned_data['email']
        if commit:
            user.save()
            profile.save()
        return profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'university', 'school', 'city', 'profile_pic']



class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'

class EventForm(ModelForm):
    class Meta:
        model = Event_s
        fields = '__all__'    

class PaintingForm(ModelForm):
    class Meta:
        model = Painting
        fields = '__all__'

class IllustrationForm(ModelForm):
    class Meta:
        model = Illustration
        fields = '__all__'    

class AbstractArtForm(ModelForm):
    class Meta:
        model = AbstractArt
        fields = '__all__'

class HandcraftForm(ModelForm):
    class Meta:
        model = Handcraft
        fields = '__all__'        

class PhotographyForm(ModelForm):
    class Meta:
        model = Photography
        fields = '__all__'      

