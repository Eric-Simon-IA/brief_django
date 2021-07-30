from .models import *
from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer pour le modèle Departement, permet la conversion des données en un flux exploitable par l'API REST
    """

    class Meta:
        model = Client
        fields = ('id', 'nom', 'prenom', 'carte_membre')


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer pour les photos, permet la conversion des données en un flux exploitable par l'API REST
    """

    picture = VersatileImageFieldSerializer(
        sizes=[
            ('full_size', 'url'),
            ('thumbnail', 'thumbnail__100x100'),
        ]
    )

    class Meta:
        model = Photo
        fields = ('id', 'dateTime', 'picture')


class HistoriqueClientSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer pour le modèle Employé, permet la conversion des données en un flux exploitable par l'API REST
    """
    face = VersatileImageFieldSerializer(
        sizes=[
            ('full_size', 'url'),
            ('thumbnail', 'thumbnail__100x100'),
        ]
    )
    # client = ClientSerializer(read_only=True)
    # photo = PhotoSerializer(read_only=True)

    class Meta:
        model = HistoriqueClient
        fields = ('id', 'client', 'photo', 'face')
