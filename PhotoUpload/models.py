from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        (0, 'Root'),
        (1, "Consultant"),
        (2, "Student"),
    )
    username = models.CharField(max_length=20, unique=True,null=True, blank=True)
    user_type = models.IntegerField(choices=USER_TYPE_CHOICES, default=0)

    def __str__(self):
        return self.email

class Users(models.Model):
    full_name = models.CharField(max_length=30)
    custom_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name='users')
    user_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(unique=True, max_length=30)
    raw_password = models.CharField(max_length=60)
    password = models.CharField(max_length=255)
    user_role = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'users'
        managed = True

    

class CardDesign(models.Model):
    card_design = models.ImageField(upload_to='card_designs', default='default_card.png')

    def __str__(self):
        return self.card_design.url  

class PhotoFrame(models.Model):
    image = models.ImageField(upload_to='photo_frame_images')
    name = models.CharField(max_length=100)
    card_design = models.ForeignKey(CardDesign, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    


class WishingCard(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100, default="FDL Family")
    background_image = models.ImageField(upload_to='wishing_card_backgrounds', default='default_background.png')

    def __str__(self):
        return self.name


