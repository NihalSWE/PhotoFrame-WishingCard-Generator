# forms.py
from django import forms
from .models import PhotoFrame, WishingCard

class PhotoFrameForm(forms.ModelForm):
    class Meta:
        model = PhotoFrame
        fields = ['image', 'name', 'card_design']



  

class WishingCardForm(forms.ModelForm):
    class Meta:
        model = WishingCard
        fields = ['name', 'designation', 'background_image']
