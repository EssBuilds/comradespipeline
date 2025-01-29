from django.contrib import admin
from .models import Player, Suspect, Weapon, Room, GameSession

admin.site.register(Player)
admin.site.register(Suspect)
admin.site.register(Weapon)
admin.site.register(Room)
admin.site.register(GameSession)
