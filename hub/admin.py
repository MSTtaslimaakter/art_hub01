from django.contrib import admin
from .models import Event_s,Artist, ArtPiece,Category, ArtPieceCategory,Painting,Illustration,AbstractArt,Handcraft,Photography
from .models import WorkshopRegistration, FestivalTicket
from .models import Profile
@admin.register(WorkshopRegistration)
class WorkshopRegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'timestamp')
    search_fields = ('name', 'email')
    list_filter = ('timestamp',)

@admin.register(FestivalTicket)
class FestivalTicketAdmin(admin.ModelAdmin):
    list_display = ('name', 'tickets', 'timestamp')
    search_fields = ('name',)
    list_filter = ('timestamp',)


admin.site.register(Profile)
admin.site.register(Event_s)
admin.site.register(Artist)
admin.site.register(ArtPiece)
admin.site.register(Category)
admin.site.register(ArtPieceCategory)
admin.site.register(Painting)
admin.site.register(Illustration)
admin.site.register(AbstractArt)
admin.site.register(Handcraft)
admin.site.register(Photography)