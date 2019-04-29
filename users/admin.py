from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Card, Deck, Hand, Game

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Card)
admin.site.register(Deck)
admin.site.register(Hand)
admin.site.register(Game)