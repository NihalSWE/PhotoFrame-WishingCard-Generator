# forms.py
from django import forms
from .models import PhotoFrame, WishingCard,CustomUser,BgImage
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
        widgets = {
            'background_image': forms.RadioSelect
        }

    def _init_(self, *args, **kwargs):
        super(WishingCardForm, self)._init_(*args, **kwargs)
        self.fields['background_image'].queryset = BgImage.objects.all()


#----Admin Panel -----
from django.contrib.auth.forms import AuthenticationForm
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            # Check if the username exists with exact case
            user = CustomUser.objects.filter(username__exact=username).first()
            if user is None:
                raise forms.ValidationError("Invalid username or password.")
            # Check if the provided password is valid for the user
            if not user.check_password(password):
                raise forms.ValidationError("Invalid username or password.")
        return self.cleaned_data
