from django.db import models
from versatileimagefield.fields import VersatileImageField, PPOIField
import os


def get_upload_path(instance, filename):
    return os.path.join('detection_client', 'detected',
                        "client_%d" % instance.client.id, filename)


# Modèles de l'application

class Client(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    carte_membre = models.IntegerField(default=0)

    def __str__(self):
        return "Nom : " + self.nom + " - Prenom : " + self.prenom + " - " \
               + ("Non membre" if self.carte_membre is None else "Numéro de membre : " + str(self.carte_membre))


class Photo(models.Model):
    dateTime = models.DateTimeField()
    picture = VersatileImageField(
        'Image',
        upload_to='detection_client/uploads/',
        ppoi_field='image_ppoi'
    )
    image_ppoi = PPOIField()


class HistoriqueClient(models.Model):
    face = VersatileImageField(
        'Image',
        upload_to=get_upload_path,
        ppoi_field='image_ppoi'
    )
    image_ppoi = PPOIField()

    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='historiques')
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='historiques')


