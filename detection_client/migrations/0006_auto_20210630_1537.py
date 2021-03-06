# Generated by Django 3.2.3 on 2021-06-30 13:37

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('detection_client', '0005_auto_20210630_1516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historiqueclient',
            name='bottom',
        ),
        migrations.RemoveField(
            model_name='historiqueclient',
            name='left',
        ),
        migrations.RemoveField(
            model_name='historiqueclient',
            name='right',
        ),
        migrations.RemoveField(
            model_name='historiqueclient',
            name='top',
        ),
        migrations.AddField(
            model_name='historiqueclient',
            name='face',
            field=versatileimagefield.fields.VersatileImageField(default='', upload_to='detection_client/detected/', verbose_name='Image'),
            preserve_default=False,
        ),
    ]
