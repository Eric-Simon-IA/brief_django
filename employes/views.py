import requests
from django.shortcuts import render, redirect
from rest_framework import viewsets

from .forms import *
from .models import *
from .serializers import DepartementSerializer, EmployeSerializer


def dep_emp(request):
    """
    Charge tous les départements avec leurs employés et les affiche dans le navigateur
    :param request: WSGIRequest
    :return: render du template de listing des départements avec leurs employés
    """
    dep_result = Departement.objects.all()

    context = {'dep_result': dep_result}
    return render(request, "employes/dep_emp.html", context)


def dep_list(request):
    """
    Charge tous les départements par appel API et les affiche dans le navigateur
    :param request: WSGIRequest
    :return: render du template de listing des départements
    """
    req = requests.get('http://127.0.0.1:8000/employes/api/dept/')
    print(req.json())

    context = {'depts': req.json()}
    return render(request, "employes/dep_list.html", context)


def dep_delete(request):
    """
    Supprime le département dont l'ID est passée en paramètres
    :param request: WSGIRequest
    :return: redirection vers la liste des départements
    """
    idDep = request.GET['id']
    req = requests.delete('http://127.0.0.1:8000/employes/api/dept/' + idDep)

    return redirect("dep_list")


def dep_detail(request):
    """
    Affiche la page de détail du département (listing des employés)
    :param request: WSGIRequest
    :return: rendering de la page détail département
    """
    idDep = request.GET['id']
    req = requests.get('http://127.0.0.1:8000/employes/api/dept/' + idDep)
    print(req.json())

    context = {'dep': req.json()}
    return render(request, "employes/dep_detail.html", context)


def emp_delete(request):
    """
    Supprime l'employé' dont l'ID est passée en paramètres
    :param request: WSGIRequest
    :return: redirectement vers la page de détail du département
    """
    idEmp = request.GET['id']
    idDep = request.GET['depid']
    req = requests.delete('http://127.0.0.1:8000/employes/api/emp/' + idEmp)

    return redirect("/employes/dep_detail?id=" + idDep)


class DepartementViewSet(viewsets.ModelViewSet):
    """
    Classe héritant du viewset du rest framework, permet de gérer automatiquement
     tous les appels API pour le modèle Departement
    """
    queryset = Departement.objects.all().order_by('intitule')
    serializer_class = DepartementSerializer


class EmployeViewSet(viewsets.ModelViewSet):
    """
    Classe héritant du viewset du rest framework, permet de gérer automatiquement
     tous les appels API pour le modèle Employe
    """
    queryset = Employe.objects.all().order_by('nom')
    serializer_class = EmployeSerializer


def dep_update_create(request):
    """
    Gère le formulaire de création ou modification de département et fait les appels API nécessaires

    :param request: WSGIRequest
    :return: redirection vers elle-même pour validation ou redirection vers la page liste des departements
    """

    # Si c'est un POST on est en réception du formulaire complété
    if request.method == 'POST':
        # création d'un form avec les paramètres réceptionnés
        form = DepForm(request.POST)
        # validation
        if form.is_valid():
            # Vérification de présence de l'id, si présente on fait un put sinon un post
            id_dep = request.POST.get('id', "")
            if id_dep == "":
                req = requests.post('http://127.0.0.1:8000/employes/api/dept/', data=request.POST)
            else:
                req = requests.put('http://127.0.0.1:8000/employes/api/dept/' + id_dep + '/', data=request.POST)
            return redirect("dep_list")

    # Si ce n'est pas un post on est au premier chargement du formulaire
    else:
        # S'il y a une id c'est une mise à jour, sinon formulaire vierge
        id = request.GET.get('id', '')
        if id != '':
            # On récupère le département
            req1 = requests.get('http://127.0.0.1:8000/employes/api/dept/' + id)
            # Et on initialise le form
            form = DepForm(initial=req1.json())
        else:
            # form vierge
            form = DepForm()

    return render(request, 'employes/dep_form.html', {'form': form})
