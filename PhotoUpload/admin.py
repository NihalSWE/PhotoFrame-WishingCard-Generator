from django.contrib import admin
from .models import PhotoFrame,WishingCard
# Register your models here.

@admin.register(PhotoFrame)
class PhotoFrameAdmin(admin.ModelAdmin):
    list_display = ('id','name','image','card_design')


@admin.register(WishingCard)
class WishingCardAdmin(admin.ModelAdmin):
    list_display=('id','name','designation', 'background_image')





