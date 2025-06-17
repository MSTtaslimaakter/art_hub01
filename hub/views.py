

from django.shortcuts import render
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login  # Import the login function
from django.contrib.auth import get_user_model
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.shortcuts import render, redirect
from .forms import WorkshopForm, FestivalForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Handcraft, HandcraftComment
from django.contrib.auth import login
from django.contrib.auth import get_user_model
User = get_user_model()
from .forms import ProfileForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ArtworkForm
from django.views.decorators.csrf import csrf_protect


@login_required
def profile_view(request):
    return render(request, 'profile.html')

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')

def home (request):
    return render (request,'home.html')

def about (request):
    return render (request,'about.html')    

def profile (request):
    return render (request,'profile.html')

def Event (request):
    return render (request,'event.html')

def workshop_view(request):
    return render(request, 'workshop.html')

def festival_view(request):
    return render(request, 'festival.html') 
def bkash_payment(request):
    data = request.session.get('booking_data', {})
    tickets = int(data.get('tickets', 0))
    amount = tickets * 150
    return render(request, 'payments/bkash.html', {'data': data, 'tickets': tickets, 'amount': amount})


def nagad_payment(request):
    data = request.session.get('booking_data', {})
    tickets = int(data.get('tickets', 0))
    amount = tickets * 150
    return render(request, 'payments/nagad.html', {'data': data, 'tickets': tickets, 'amount': amount})

    

def rocket_payment(request):
    data = request.session.get('booking_data', {})
    tickets = int(data.get('tickets', 0))
    amount = tickets * 150
    return render(request, 'payments/rocket.html', {
        'data': data,
        'tickets': tickets,
        'amount': amount
    })


def card_payment(request):
    data = request.session.get('booking_data', {})
    tickets = int(data.get('tickets', 0))
    amount = tickets * 150
    return render(request, 'payments/card.html', {'data': data, 'tickets': tickets, 'amount': amount})



def exhibition_view(request):
    return render(request, 'exhibition.html')

def sign_up(request):
    return render (request,'sign_up.html')

def log_in (request):
    return render (request,'log_in.html')

def Gallery (request):
    return render (request,'gallery.html')

def Artist_profile (request):
    return render (request, 'artist_profile.html')


def payment(request):
    return render(request, 'payment.html') 

def purchase (request):
    return render (request, 'purchase.html')

def paintings (request):
    return render (request, 'paintings.html')
def illustrations (request):
    return render (request, 'illustrations.html')
def handcraft(request):
    return render(request, 'handcraft.html')
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

def Handcrafts(request):
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

def abstractart(request):
    artworks = AbstractArt.objects.all()
    return render(request, 'abstractart.html', {'artworks': artworks})

def bkash_payment(request):
    ticket_data = request.session.get('ticket_data', {})
    return render(request, 'payments/bkash.html', {'data': ticket_data})


def nagad_payment(request):
    ticket_data = request.session.get('ticket_data', {})
    return render(request, 'payments/nagad.html', {'data': ticket_data})

def rocket_payment(request):
    ticket_data = request.session.get('ticket_data', {})
    return render(request, 'payments/rocket.html', {'data': ticket_data})

def card_payment(request):
    ticket_data = request.session.get('ticket_data', {})
    return render(request, 'payments/card.html', {'data': ticket_data})



def payment(request):
    if request.method == "POST":

        return redirect('purchase')

    return render(request, 'payment.html')


def purchase(request):
    return render(request, 'purchase.html')

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


def event_detail(request, type):
    submitted = False
    form = None

    if type == 'workshop':
        if request.method == 'POST':
            form = WorkshopForm(request.POST)
            if form.is_valid():
                form.save()
                submitted = True
        else:
            form = WorkshopForm()

    elif type == 'festival':
        if request.method == 'POST':
            form = FestivalForm(request.POST)
            if form.is_valid():
                form.save()
                submitted = True
        else:
            form = FestivalForm()

    return render(request, 'event_detail.html', {
        'event_type': type,
        'form': form,
        'submitted': submitted
    })



def workshop(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        payment_method = request.POST.get('payment_method')

        # Save registration data in session for payment pages
        request.session['workshop_data'] = {
            'name': name,
            'email': email,
            'contact': contact,
            'payment_method': payment_method,
        }

        # Redirect to payment page based on selected payment method
        if payment_method == 'bkash':
            return redirect('bkash_payment')
        elif payment_method == 'nagad':
            return redirect('nagad_payment')
        elif payment_method == 'rocket':
            return redirect('rocket_payment')
        elif payment_method == 'card':
            return redirect('card_payment')

        # Invalid payment method
        return render(request, 'workshop.html', {'error': 'Invalid payment method'})

    return render(request, 'workshop.html')




# views.py

def exhibition_ticket(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        tickets = request.POST.get('tickets')
        payment_method = request.POST.get('payment_method')

        # Store data in session to show later
        request.session['ticket_data'] = {
            'name': name,
            'email': email,
            'contact': contact,
            'tickets': tickets,
        }

        # Redirect based on selected payment method
        if payment_method == 'bkash':
            return redirect('bkash_payment')
        elif payment_method == 'nagad':
            return redirect('nagad_payment')
        elif payment_method == 'rocket':
            return redirect('rocket_payment')
        elif payment_method == 'card':
            return redirect('card_payment')
        else:
            return render(request, 'exhibition_ticket.html', {'error': 'Invalid payment method'})

    return render(request, 'exhibition_ticket.html')


@csrf_protect
def festival(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        tickets = request.POST.get('tickets')
        payment_method = request.POST.get('payment_method')

        # Save booking data here (if needed)

        # Redirect to appropriate payment page
        if payment_method == 'bkash':
            return redirect('bkash_payment')
        elif payment_method == 'nagad':
            return redirect('nagad_payment')
        elif payment_method == 'rocket':
            return redirect('rocket_payment')
        elif payment_method == 'credit_card':
            return redirect('card_payment')
        else:
            return redirect('festival')  # fallback

    return render(request, 'festival.html')




def handcraft_gallery(request):
    handcrafts = Handcraft.objects.all()
    return render(request, 'your_template_folder/handcraft_gallery.html', {'handcrafts': handcrafts})



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
    handcraft = get_object_or_404(handcraft, id=id)
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

def login_view(request):
    error = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')  # Successfully logged in
        else:
            error = "Invalid username or password."
    
    return render(request, 'log_in.html', {'error': error})  # Pass error to template


def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('password2')  # এখানে 'password2' ব্যবহার করো

        if password != confirm_password:
            return render(request, 'sign_up.html', {'error': "Passwords do not match."})

        if User.objects.filter(username=username).exists():
            return render(request, 'sign_up.html', {'error': "Username already taken."})

        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        return redirect('profile')

    return render(request, 'sign_up.html')



def add_comment(request, painting_id):
    painting = Painting.objects.get(id=painting_id)  # Get the painting
    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        if comment_text:
            # Save the comment to the database
            comment.objects.create(painting=painting, text=comment_text)
        return redirect('paintings')  # Redirect back to the paintings page
    return redirect('paintings')  # Redirect back if the method is not POST

def create_user_view(request):
    User = get_user_model()
    User.objects.create_user(username='john', password='john123')
    return HttpResponse("User created")
# views.py
@login_required
def Profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    # Example placeholders — replace with real queries
    artworks = Artwork.objects.filter(artist=request.user)  # If you have an Artwork model
    favorite_artists = profile.favorite_artists.all() if hasattr(profile, 'favorite_artists') else []
    joined_events = Event.objects.filter(participants=request.user)  # Assuming many-to-many

    return render(request, 'profile.html', {
        'user': request.user,
        'artworks': artworks,
        'favorite_artists': favorite_artists,
        'joined_events': joined_events,
    })

@login_required
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Make sure 'profile' is the correct name in urls.py
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {'form': form})


@login_required
def upload_artwork(request):
    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            artwork = form.save(commit=False)
            artwork.artist = request.user
            artwork.save()
            return redirect('profile')  # or any success page
    else:
        form = ArtworkForm()

    return render(request, 'upload_artwork.html', {'form': form})




# Create your views here.

