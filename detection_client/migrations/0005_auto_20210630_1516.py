# Generated by Django 3.2.3 on 2021-06-30 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detection_client', '0004_alter_client_carte_membre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historiqueclient',
            name='etat',
        ),
        migrations.DeleteModel(
            name='Etat',
        ),
    ]
