from django.contrib import admin
from .models import PhotoFrame, WishingCard, CardDesign,BgImage

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


@admin.register(BgImage)
class BgImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'background_image')


from .models import CustomUser

admin.site.register(CustomUser)