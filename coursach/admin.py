from django.contrib import admin
from .models import *

class PetitionAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'tour']

class TourAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']

admin.site.register(TourPetition, PetitionAdmin)
admin.site.register(Tour, TourAdmin)

