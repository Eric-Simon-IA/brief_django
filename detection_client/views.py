import requests
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from .detect.detect_face_reco import get_recognition
from .forms import HistoForm, PhotoForm
from .models import *
from datetime import datetime
from .serializers import ClientSerializer, HistoriqueClientSerializer, PhotoSerializer
from rest_framework.parsers import MultiPartParser


class ClientViewSet(viewsets.ModelViewSet):
    """
    Classe héritant du viewset du rest framework, permet de gérer automatiquement
     tous les appels API pour le modèle Employe
    """
    queryset = Client.objects.all().order_by('nom')
    serializer_class = ClientSerializer


class HistoriqueViewSet(viewsets.ModelViewSet):
    """
    Classe héritant du viewset du rest framework, permet de gérer automatiquement
     tous les appels API pour le modèle Employe
    """
    queryset = HistoriqueClient.objects.all().order_by('id')
    serializer_class = HistoriqueClientSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    """
    Classe héritant du viewset du rest framework, permet de gérer automatiquement
     tous les appels API pour le modèle Employe
    """
    queryset = Photo.objects.all().order_by('id')
    serializer_class = PhotoSerializer


def clients(request):
    """
    Charge tous les départements avec leurs employés et les affiche dans le navigateur
    :param request: WSGIRequest
    :return: render du template de listing des départements avec leurs employés
    """
    cli_result = Client.objects.all()

    context = {'cli_result': cli_result}
    return render(request, "detection/clients.html", context)


def client_detail(request):
    """
    Affiche la page de détail du client (listing des historiques de vue)
    :param request: WSGIRequest
    :return: rendering de la page détail département
    """
    idClient = request.GET['id']
    historiques_o = HistoriqueClient.objects.filter(client_id=idClient)
    req = requests.get('http://127.0.0.1:8000/detection_client/api/clients/' + idClient)
    print(req.json())
    historiques = []
    for hist in historiques_o:
        dic_hist_ser = HistoriqueClientSerializer(hist, context={'request': request}).data
        dic_hist_ser['photo'] = hist.photo
        dic_hist_ser['client'] = hist.client
        historiques.append(dic_hist_ser)
    context = {'cli': req.json(), 'historiques': historiques}
    return render(request, "detection/histo_client.html", context)


def photos(request):
    """
    Charge toutes les photos
    :param request: WSGIRequest
    :return: render du template de listing des photos
    """

    req = requests.get('http://127.0.0.1:8000/detection_client/api/photo/')
    print(req.json())

    context = {'photo_result': req.json()}
    return render(request, "detection/photos.html", context)


def det_photo(request):
    """
    Charge une photo et les visage identifiés
    :param request: WSGIRequest
    :return: render du template de détail de la photo
    """
    idPhoto = request.GET['id']
    photo = Photo.objects.get(id=idPhoto)

    res_histo = photo.historiques.all()
    if len(res_histo) == 0:
        bblst, pictures = get_recognition(photo.picture.path, photo)
        res_histo = photo.historiques.all()

    historiques = []
    for hist in res_histo:
        dic_hist_ser = HistoriqueClientSerializer(hist, context={'request': request}).data
        dic_hist_ser['photo'] = hist.photo
        dic_hist_ser['client'] = hist.client
        historiques.append(dic_hist_ser)

    context = {'photo_result': photo, 'historiques': historiques}
    return render(request, "detection/det_photo.html", context)


def histo_edit(request, id=None):
    """
    Charge une photo et les visage identifiés
    :param id:
    :param request: WSGIRequest
    :return: render du template de détail de la photo
    """
    histmod = get_object_or_404(HistoriqueClient, id=id)
    if request.method == "POST":
        form = HistoForm(request.POST,
                         instance=histmod)
        if form.is_valid():

            values = {'client': "http://127.0.0.1:8000/detection_client/api/clients/" + str(form.data['client']) + "/",
                      'photo': "http://127.0.0.1:8000/detection_client/api/photo/" + str(histmod.photo.id) + "/"}
            files = {'face': histmod.face.open()}

            r = requests.post("http://127.0.0.1:8000/detection_client/api/histo/", data=values, files=files)

            if r.status_code < 400:
                histmod.face.delete_all_created_images()
                histmod.face.delete(save=False)
                histmod.delete()

            return redirect("/detection_client/det_photo?id=" + str(histmod.photo.id))
    else:
        form = HistoForm(instance=histmod)
    dic_hist = HistoriqueClientSerializer(histmod, context={'request': request}).data
    return render(request,
                  'detection/hist_edit.html',
                  {
                      'form': form,
                      'hist': histmod,
                      'dic_hist': dic_hist
                  })


def new_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)

        if form.is_valid():
            newPhoto = form.save()
            return redirect("/detection_client/det_photo?id=" + str(newPhoto.id))
    else:
        form = PhotoForm()
    return render(request, 'detection/new_photo.html', {'form': form})
