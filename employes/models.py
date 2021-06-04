from django.db import models


# Modèles de l'application

class Departement(models.Model):
    intitule = models.CharField(max_length=30)
    etage = models.IntegerField()

    def __str__(self):
        return "Département : " + self.intitule + " - Etage : " + str(self.etage)


class Employe(models.Model):
    prenom = models.CharField(max_length=30)
    nom = models.CharField(max_length=30)
    ville = models.CharField(max_length=30)
    poste = models.CharField(max_length=30)
    age = models.IntegerField()
    salaire = models.DecimalField(max_digits=12, decimal_places=2)
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE,related_name='employes')

    def __str__(self):
        return "Nom complet : " + self.nom + " " + self.prenom + " - Ville : " + self.ville + " - Poste : " + self.poste
