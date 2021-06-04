from .models import *
from rest_framework import serializers


class EmployeSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer pour le modèle Employé, permet la conversion des données en un flux exploitable par l'API REST
    """
    class Meta:
        model = Employe
        fields = ('id', 'nom', 'prenom', 'ville', 'poste', 'age', 'salaire', 'departement_id')


class DepartementSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer pour le modèle Departement, permet la conversion des données en un flux exploitable par l'API REST
    """
    # Ajout du lien one to many vers les employés, permet de les inclure dans le flux
    # Read_only à True pour ne pas autoriser la modification des employés via les départements
    employes = EmployeSerializer(read_only=True, many=True)

    class Meta:
        model = Departement
        fields = ('id', 'intitule', 'etage', 'employes')
