# forms.py
from django import forms
from .models import PhotoFrame, WishingCard
import os
class PhotoFrameForm(forms.ModelForm):
    card_design_choices = [
        ('card_design_1.png', 'Card Design 1'),
        ('card_design_2.png', 'Card Design 2'),
    ]

    card_design = forms.ChoiceField(choices=card_design_choices, widget=forms.RadioSelect)

    class Meta:
        model = PhotoFrame
        fields = ['image', 'name', 'card_design']

    def clean_card_design(self):
        card_design = self.cleaned_data.get('card_design')
        return os.path.join('card_designs', card_design)

class WishingCardForm(forms.ModelForm):
    class Meta:
        model = WishingCard
        fields = ['name', 'designation', 'background_image']
