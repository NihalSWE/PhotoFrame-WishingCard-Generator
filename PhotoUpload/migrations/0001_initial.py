# Generated by Django 4.2.7 on 2024-05-15 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CardDesign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_design', models.ImageField(default='default_card.png', upload_to='card_designs')),
            ],
        ),
        migrations.CreateModel(
            name='WishingCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('designation', models.CharField(default='FDL Family', max_length=100)),
                ('background_image', models.ImageField(default='default_background.png', upload_to='wishing_card_backgrounds')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoFrame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photo_frame_images')),
                ('name', models.CharField(max_length=100)),
                ('card_design', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PhotoUpload.carddesign')),
            ],
        ),
    ]
