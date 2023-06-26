from django.contrib import admin
from .models import Dog, Spice


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ('name', 'specie', 'birthdate')
    list_filter = ('specie',)


@admin.register(Spice)
class SpiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')