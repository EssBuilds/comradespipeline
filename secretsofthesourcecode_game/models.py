from django.db import models
import random


class Suspect(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Weapon(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Scenario(models.Model):
    title = models.CharField(max_length=255)  # Name of the scenario
    description = models.TextField()  # Story details
    correct_suspect = models.ForeignKey(Suspect, on_delete=models.CASCADE)
    correct_weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE)
    correct_room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @classmethod
    def get_random_scenario(cls):
        return cls.objects.order_by("?").first()
