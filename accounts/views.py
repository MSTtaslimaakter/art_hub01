# accounts/views.py
from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def registration_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Set the user's roles
            if form.cleaned_data['is_admin']:
                user.is_admin = True
            if form.cleaned_data['is_artist']:
                user.is_artist = True
            if form.cleaned_data['is_consumer']:
                user.is_consumer = True
            user.save()
            return redirect('login')
    else:
        form = SignupForm()

    return render(request, 'accounts/registration.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_admin:
                    return redirect('admin_dashboard')
                elif user.is_artist:
                    return redirect('artist_dashboard')
                elif user.is_consumer:
                    return redirect('consumer_dashboard')
                else:
                    return redirect('home')
            else:
                return redirect('login')
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})

# accounts/views.py
from django.shortcuts import render

def admin_dashboard(request):
    return render(request, 'accounts/admin_dashboard.html')

def artist_dashboard(request):
    return render(request, 'accounts/artist_dashboard.html')

def consumer_dashboard(request):
    return render(request, 'accounts/consumer_dashboard.html')

