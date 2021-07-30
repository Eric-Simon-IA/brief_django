from datetime import datetime

from django.forms import ModelForm
from detection_client.models import HistoriqueClient, Photo
from django.contrib.admin import widgets


class HistoForm(ModelForm):
    class Meta:
        model = HistoriqueClient
        fields = ['client']

    def is_valid(self):
        return True


class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ['picture','dateTime']

    def is_valid(self):
        return True

    def __init__(self, *args, **kwargs):
        super(PhotoForm, self).__init__(*args, **kwargs)
        self.initial['dateTime'] = datetime.now()

