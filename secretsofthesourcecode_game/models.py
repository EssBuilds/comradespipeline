from django.db import models
import random

class Player(models.Model):
    name = models.CharField(max_length=100)

class Suspect(models.Model):
    name = models.CharField(max_length=100)

class Weapon(models.Model):
    name = models.CharField(max_length=100)

class Room(models.Model):
    name = models.CharField(max_length=100)

class GameSession(models.Model):
    players = models.ManyToManyField(Player)
    secret_suspect = models.ForeignKey(Suspect, on_delete=models.CASCADE, related_name='secret_suspect')
    secret_weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE, related_name='secret_weapon')
    secret_room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='secret_room')
    is_active = models.BooleanField(default=True)

    @classmethod
    def create_new_game(cls):
        suspects = list(Suspect.objects.all())
        weapons = list(Weapon.objects.all())
        rooms = list(Room.objects.all())

        if not (suspects and weapons and rooms):
            raise ValueError("Ensure all categories have data!")

        return cls.objects.create(
            secret_suspect=random.choice(suspects),
            secret_weapon=random.choice(weapons),
            secret_room=random.choice(rooms)
        )
