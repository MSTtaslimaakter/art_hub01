
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
def Home (request):
    return render (request,'home.html')

def About (request):
    return render (request,'about.html')    

def Profile (request):
    return render (request,'profile.html')

def Event (request):
    return render (request,'event.html')

def Sign_in (request):
    return render (request,'sign_in.html')

def Log_in (request):
    return render (request,'log_in.html')

def Gallery (request):
    return render (request,'gallery.html')

def Artist_profile (request):
    return render (request, 'artist_profile.html')

def payment (request):
    return render (request, 'payment.html')

def purchase (request):
    return render (request, 'purchase.html')

def paintings (request):
    return render (request, 'paintings.html')
def illustrations (request):
    return render (request, 'illustrations.html')
def handcrafts (request):
    return render (request, 'handcraft.html')
def photography (request):
    return render (request, 'photography.html')
def abstractart (request):
    return render (request, 'abstractart.html')


# Create your views here.

def home(request):
    art= Event_s.objects.all()
    context= {
        'art': art,
    }

    return render (request,'home.html',context=context)
def about(request):
    art= Event_s.objects.all()
    context= {
        'art': art,
    }

    return render (request,'about.html',context=context)
def artist(request):
    artists=Artist.objects.all()
    context={
       'artists': artists,
    }
    return render (request,'artist_profile.html',context=context)
def event_page(request):
    events = Event_s.objects.all()  # Fetch all events from the correct model
    context = {
        'events': events
    }
    return render(request, 'event.html', context)

def paintings(request):
    paintings = Painting.objects.all()  # Fetch all paintings from the database
    context = {
        'paintings': paintings
    }
    return render(request, 'paintings.html', context)

def illustrations(request):
    illustrations = Illustration.objects.all()  # Fetch all illustrations from the database
    context = {
        'illustrations': illustrations
    }
    return render(request, 'illustrations.html', context)

def handcrafts(request):
    handcrafts = Handcraft.objects.all()  # Get all handcrafts from the database
    context = {
        'handcrafts': handcrafts
    }
    return render(request, 'handcraft.html', context)

def photography(request):
    photos = Photography.objects.all()  # Fetch all photography objects from the database
    context = {
        'photos': photos
    }
    return render(request, 'photography.html', context)

def abstractart(request):
    artworks = AbstractArt.objects.all()  # Fetch all abstract art objects from the database
    context = {
        'artworks': artworks
    }
    return render(request, 'abstractart.html', context)

def artist_profile_details(request, artist_id):
    # Fetch the artist based on the artist_id (primary key)
    artist = get_object_or_404(Artist, artist_id=artist_id)
    return render(request, 'artist_profile_details.html', {'artist': artist})

def create_artist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('artist_profile')
    else:
        form = ArtistForm()
    return render(request, 'artist_form.html', {'form': form})

# Update operation: Form for updating an existing artist
def update_artist(request, artist_id):
    artist = get_object_or_404(Artist, artist_id=artist_id)
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES, instance=artist)
        if form.is_valid():
            form.save()
            return redirect('artist_profile')
    else:
        form = ArtistForm(instance=artist)
    return render(request, 'artist_form.html', {'form': form, 'artist': artist})

# Delete operation: Delete an artist
def delete_artist(request, artist_id):
    artist = get_object_or_404(Artist, artist_id=artist_id)
    artist.delete()
    return redirect('artist_profile')

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the event
            return redirect('event')  # Redirect to the event page after saving
    else:
        form = EventForm()
    return render(request, 'create_event.html', {'form': form})

def update_event(request, event_id):
    event = get_object_or_404(Event_s, id=event_id)
    
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event')  # Redirect to events page after update
    else:
        form = EventForm(instance=event)
    
    return render(request, 'update_event.html', {'form': form})



def delete_event(request, event_id):
    event = get_object_or_404(Event_s, id=event_id)
    event.delete()
    return redirect('event')  # Redirect to events page after deletion

def create_painting(request):
    if request.method == 'POST':
        form = PaintingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')  # Redirect to the gallery page after saving
    else:
        form = PaintingForm()
    return render(request, 'create_painting.html', {'form': form})

def update_painting(request, painting_id):
    painting = get_object_or_404(Painting, id=painting_id)
    if request.method == 'POST':
        form = PaintingForm(request.POST, request.FILES, instance=painting)
        if form.is_valid():
            form.save()
            return redirect('gallery')  # Redirect to the gallery page after updating
    else:
        form = PaintingForm(instance=painting)
    return render(request, 'update_painting.html', {'form': form, 'painting': painting})

def delete_painting(request, painting_id):
    painting = get_object_or_404(Painting, id=painting_id)
    if request.method == 'POST':
        painting.delete()
        return redirect('gallery')  # Redirect to the gallery page after deletion
    return render(request, 'delete_painting.html', {'painting': painting})

def create_illustration(request):
    if request.method == 'POST':
        form = IllustrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('illustrations')  # Redirect to illustrations page
    else:
        form = IllustrationForm()
    return render(request, 'create_illustration.html', {'form': form})

# View to update an existing illustration
def update_illustration(request, id):
    illustration = get_object_or_404(Illustration, id=id)
    if request.method == 'POST':
        form = IllustrationForm(request.POST, request.FILES, instance=illustration)
        if form.is_valid():
            form.save()
            return redirect('illustrations')  # Redirect to illustrations page
    else:
        form = IllustrationForm(instance=illustration)
    return render(request, 'update_illustration.html', {'form': form, 'illustration': illustration})

# View to delete an illustration
def delete_illustration(request, id):
    illustration = get_object_or_404(Illustration, id=id)
    if request.method == 'POST':
        illustration.delete()
        return redirect('illustrations')  # Redirect to illustrations page
    return render(request, 'delete_illustration.html', {'illustration': illustration})

def create_abstractart(request):
    if request.method == 'POST':
        form = AbstractArtForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('abstractart')  # Redirect back to the list of artworks
    else:
        form = AbstractArtForm()
    return render(request, 'create_abstractart.html', {'form': form})

# Update existing abstract art
def update_abstractart(request, id):
    art = get_object_or_404(AbstractArt, id=id)
    if request.method == 'POST':
        form = AbstractArtForm(request.POST, request.FILES, instance=art)
        if form.is_valid():
            form.save()
            return redirect('abstractart')
    else:
        form = AbstractArtForm(instance=art)
    return render(request, 'update_abstractart.html', {'form': form})

# Delete existing abstract art
def delete_abstractart(request, id):
    art = get_object_or_404(AbstractArt, id=id)
    if request.method == 'POST':
        art.delete()
        return redirect('abstractart')
    return render(request, 'delete_abstractart.html', {'art': art})

def create_handcraft(request):
    if request.method == 'POST':
        form = HandcraftForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('handcrafts')  # Redirect back to the list of handcrafts
    else:
        form = HandcraftForm()
    return render(request, 'create_handcraft.html', {'form': form})
def update_handcraft(request, id):
    handcraft = get_object_or_404(Handcraft, id=id)
    if request.method == 'POST':
        form = HandcraftForm(request.POST, request.FILES, instance=handcraft)
        if form.is_valid():
            form.save()
            return redirect('handcrafts')
    else:
        form = HandcraftForm(instance=handcraft)
    return render(request, 'update_handcraft.html', {'form': form})

# Delete existing handcraft
def delete_handcraft(request, id):
    handcraft = get_object_or_404(Handcraft, id=id)
    if request.method == 'POST':
        handcraft.delete()
        return redirect('handcrafts')
    return render(request, 'delete_handcraft.html', {'handcraft': handcraft})

def create_photography(request):
    if request.method == 'POST':
        form = PhotographyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('photography')  # Redirect back to the photography gallery page
    else:
        form = PhotographyForm()
    return render(request, 'create_photography.html', {'form': form})

def update_photography(request, id):
    photo = get_object_or_404(Photography, id=id)
    if request.method == 'POST':
        form = PhotographyForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('photography')  # Redirect back to the photography gallery page
    else:
        form = PhotographyForm(instance=photo)
    return render(request, 'update_photography.html', {'form': form})

def delete_photography(request, id):
    photo = get_object_or_404(Photography, id=id)
    if request.method == 'POST':
        photo.delete()
        return redirect('photography')  # Redirect back to the photography gallery page
    return render(request, 'delete_photography.html', {'photo': photo})

