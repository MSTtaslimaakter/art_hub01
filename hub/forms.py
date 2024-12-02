from django.forms import ModelForm
from .models import *

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