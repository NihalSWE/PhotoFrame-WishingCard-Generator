from django.db import models

class PhotoFrame(models.Model):
    image = models.ImageField(upload_to='photo_frame_images')
    name = models.CharField(max_length=100)
    card_design = models.ImageField(upload_to='card_designs', default='default_card.png')

    def __str__(self):
        return self.name

class WishingCard(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100,default="FDL Family")
    background_image = models.ImageField(upload_to='wishing_card_backgrounds', default='default_background.png')

    def __str__(self):
        return self.name
    

