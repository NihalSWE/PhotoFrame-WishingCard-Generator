from django.contrib import admin
from .models import PhotoFrame, WishingCard, CardDesign

# Register your models here.

@admin.register(PhotoFrame)
class PhotoFrameAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')

@admin.register(WishingCard)
class WishingCardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'designation', 'background_image')

@admin.register(CardDesign)
class CardDesignAdmin(admin.ModelAdmin):
    list_display = ('id', 'card_design')

from .models import CustomUser

admin.site.register(CustomUser)