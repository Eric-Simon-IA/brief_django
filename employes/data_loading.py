"""
Chargement des données par défaut pour la bdd
"""
from employes.models import *

dep1 = Departement(intitule="Bioméchanique", etage=-4)
dep1.save()
dep2 = Departement(intitule="Administration", etage=1)
dep2.save()

emp = Employe()
emp.nom = "Simon"
emp.prenom = "Eric"
emp.age = 33
emp.ville = "Lingolsheim"
emp.salaire = 78255.14
emp.poste = "Responsable scientifique"
emp.departement = dep1
emp.save()

emp = Employe()
emp.nom = "Simon"
emp.prenom = "Mireille"
emp.age = 33
emp.ville = "Lingolsheim"
emp.salaire = 48324
emp.poste = "Expert comptable"
emp.departement = dep2
emp.save()

emp = Employe()
emp.nom = "Alia"
emp.prenom = "Random"
emp.age = 28
emp.ville = "Illkirch"
emp.salaire = 26741
emp.poste = "Assistante comptable"
emp.departement = dep2
emp.save()

emp = Employe()
emp.nom = "Bouvier"
emp.prenom = "Nicolas"
emp.age = 35
emp.ville = "Strasbourg"
emp.salaire = 15.14
emp.poste = "Minion"
emp.departement = dep1
emp.save()

emp = Employe()
emp.nom = "Colombert"
emp.prenom = "Mathieu"
emp.age = 38
emp.ville = "Strasbourg"
emp.salaire = 0
emp.poste = "Sujet d'expérience"
emp.departement = dep1
emp.save()
