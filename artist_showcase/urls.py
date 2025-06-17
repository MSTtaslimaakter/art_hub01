"""
URL configuration for artist_showcase project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from hub import views 
from .import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('profile/', views.profile_view, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('upload_artwork/', views.upload_artwork, name='upload_artwork'),
    path('event/', views.event_page, name='event'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('log_in/', views.login_view, name='log_in'),
    path('logout/', views.logout_view, name='logout'),
    path('gallery/', views.Gallery, name='gallery'),
    path('artist_profile/',views.artist,name='artist_profile'),
    path('payment/',views.payment,name='payment'),
    path('purchase/',views.purchase,name='purchase'),
    path('paintings/', views.paintings, name='paintings'),
    path('illustrations/', views.illustrations, name='illustrations'),
    path('handcraft/', views.handcraft, name='handcraft'),
    path('photography/', views.photography, name='photography'),
    path('abstractart/', views.abstractart, name='abstractart'),
    path('artist/<int:artist_id>/', views.artist_profile_details, name='artist_profile_details'),
    path('artists/', views.artist, name='artist_profile'),
    path('artists/create/', views.create_artist, name='create_artist'),
    path('artists/update/<int:artist_id>/', views.update_artist, name='update_artist'),
    path('artists/delete/<int:artist_id>/', views.delete_artist, name='delete_artist'),
    path('create/', views.create_event, name='create_event'),
    path('update/<int:event_id>/', views.update_event, name='update_event'),
    path('delete/<int:event_id>/', views.delete_event, name='delete_event'),
    path('event/<str:type>/', views.event_detail, name='event_detail'),
    path('workshop/', views.workshop_view, name='workshop'),
    path('festival/', views.festival_view, name='festival'),
    path('payment/bkash/', views.bkash_payment, name='bkash_payment'),
    path('payment/nagad/', views.nagad_payment, name='nagad_payment'),
    path('payment/rocket/', views.rocket_payment, name='rocket_payment'),
    path('payment/card/', views.card_payment, name='card_payment'),
    path('exhibition/', views.exhibition_view, name='exhibition'),
    path('exhibition-ticket/', views.exhibition_ticket, name='exhibition_ticket'),
    path('create_painting/', views.create_painting, name='create_painting'),
    path('update_painting/<int:painting_id>/', views.update_painting, name='update_painting'),
    path('delete_painting/<int:painting_id>/', views.delete_painting, name='delete_painting'),
    path('create_illustration/', views.create_illustration, name='create_illustration'),
    path('update_illustration/<int:id>/', views.update_illustration, name='update_illustration'),
    path('delete_illustration/<int:id>/', views.delete_illustration, name='delete_illustration'),
    path('create_abstractart/', views.create_abstractart, name='create_abstractart'),
    path('update_abstractart/<int:id>/', views.update_abstractart, name='update_abstractart'),
    path('delete_abstractart/<int:id>/', views.delete_abstractart, name='delete_abstractart'),
    path('create_handcraft/', views.create_handcraft, name='create_handcraft'),
    path('update_handcraft/<int:id>/', views.update_handcraft, name='update_handcraft'),
    path('delete_handcraft/<int:id>/', views.delete_handcraft, name='delete_handcraft'),
    path('create_photography/', views.create_photography, name='create_photography'),
    path('update_photography/<int:id>/', views.update_photography, name='update_photography'),
    path('delete_photography/<int:id>/', views.delete_photography, name='delete_photography'),
    path('handcraft/', views.handcraft, name='handcraft'),
    path('payment/', views.payment, name='payment'),
    path('accounts/', include('accounts.urls')),
    path('add_comment/<int:painting_id>/', views.add_comment, name='add_comment'),  # URL for adding a comment
    path('chatbot/', include('chatbot.urls')),

    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

