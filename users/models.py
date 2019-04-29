from django.contrib.auth.models import AbstractUser

from django.db import models

class CustomUser(AbstractUser):
    pass

class Game(models.Model):
    date_started = models.DateTimeField('date started')
    date_finished = models.DateTimeField('date finished')
    player = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    in_progress = models.BooleanField(default=True)
    game_won = models.BooleanField(default=True)

class Hand(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

class Deck(models.Model):
    title = models.CharField(max_length=255)
    game = models.OneToOneField(
        Game,
        on_delete=models.CASCADE,
        primary_key=True,
    )

class Card(models.Model):
    title = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    deck = models.ManyToManyField(Deck)
    hand = models.ManyToManyField(Hand)
    physical_strength = models.IntegerField()
    fear_factor = models.IntegerField()
    killing_power = models.IntegerField()
    horror_rating = models.IntegerField()

    def __str__(self):
        return self.title
