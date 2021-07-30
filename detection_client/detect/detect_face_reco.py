import tempfile

import face_recognition
import requests
from PIL import Image
from django.conf import settings
from deepface import DeepFace
from detection_client.models import *
import pathlib
import re


def create_histo(photo, temp_face_file, idCli):
    if idCli is None:
        def_cli = Client.objects.get(nom=settings.DEFAULT_USER)
    else:
        def_cli = Client.objects.get(id=idCli)

    values = {'client': "http://127.0.0.1:8000/detection_client/api/clients/" + str(def_cli.id) + "/",
              'photo': "http://127.0.0.1:8000/detection_client/api/photo/" + str(photo.id) + "/"}
    files = {'face': open(temp_face_file, 'rb')}

    r = requests.post("http://127.0.0.1:8000/detection_client/api/histo/", data=values, files=files)
    print(r)


def get_reco_client_id(face_array):
    df = DeepFace.find(img_path=face_array, db_path=settings.IMG_DB_PATH, detector_backend="retinaface",
                       enforce_detection=False, model=settings.MODEL)

    if len(df) > 0 and df.iloc[0]['VGG-Face_cosine'] < 0.3:
        path = pathlib.PurePath(df.iloc[0]['identity'])
        folder = path.parent.name
        idCli = re.match('.*?([0-9]+)$', folder).group(1)
    else:
        idCli = None

    return idCli


def get_recognition(image_path, photo):
    image = face_recognition.load_image_file(image_path)
    face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=1, model='cnn')

    for face_location in face_locations:
        top, right, bottom, left = face_location

        # You can access the actual face itself like this:
        face_image = image[top:bottom, left:right]

        idCli = get_reco_client_id(face_image)

        pil_image = Image.fromarray(face_image)

        with tempfile.NamedTemporaryFile(mode="wb", delete=False, suffix='.jpg') as jpg:
            name = jpg.name

        pil_image.save(name)
        create_histo(photo, name, idCli)

    return face_locations, face_image
