from django.contrib import admin
from .models import Suspect, Weapon, Room, Scenario

admin.site.register(Suspect)
admin.site.register(Weapon)
admin.site.register(Room)
admin.site.register(Scenario)
