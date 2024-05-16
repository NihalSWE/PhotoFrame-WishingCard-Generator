from django import forms
from django.utils.safestring import mark_safe

from django import forms
from django.utils.safestring import mark_safe

class ImageRadioSelect(forms.RadioSelect):
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subindex=subindex, attrs=attrs)
        # Generate the image URL and add it to the option's label
        image_url = f'{value}'
        option['image_url'] = image_url
        option['label'] = mark_safe(f'<img src="{image_url}" style="width: 100px; height: auto;"> ')
        return option
