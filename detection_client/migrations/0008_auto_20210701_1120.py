# Generated by Django 3.2.3 on 2021-07-01 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detection_client', '0007_historiqueclient_image_ppoi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historiqueclient',
            name='client',
        ),
        migrations.RemoveField(
            model_name='historiqueclient',
            name='photo',
        ),
    ]
