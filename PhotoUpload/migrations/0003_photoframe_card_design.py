# Generated by Django 4.2.7 on 2024-05-11 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PhotoUpload', '0002_alter_photoframe_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='photoframe',
            name='card_design',
            field=models.ImageField(default='default_card.png', upload_to='card_designs'),
        ),
    ]
