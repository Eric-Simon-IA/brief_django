import pickle

from deepface.DeepFace import represent
from django.apps import AppConfig
import os
from django.conf import settings
from tqdm import tqdm


def build_database_file(file_name):
    employees = []

    for r, d, f in os.walk(settings.IMG_DB_PATH):  # r=root, d=directories, f = files
        for file in f:
            if ('.jpg' in file.lower()) or ('.png' in file.lower()):
                exact_path = r + "/" + file
                employees.append(exact_path)

    if len(employees) == 0:
        raise ValueError("There is no image in ", settings.IMG_DB_PATH, "folder! Validate .jpg or .png files exist in "
                                                                        "this path.")

    # ------------------------
    # find representations for db images

    representations = []

    pbar = tqdm(range(0, len(employees)), desc='Finding representations', disable=False)

    # for employee in employees:
    for index in pbar:
        employee = employees[index]

        instance = []
        instance.append(employee)

        representation = represent(img_path=employee
                                   , model_name=settings.MODEL_NAME, model=settings.MODEL
                                   , enforce_detection=False, detector_backend="retinaface"
                                   , align=True)

        instance.append(representation)

        # -------------------------------

        representations.append(instance)

    f = open(settings.IMG_DB_PATH + '/' + file_name, "wb")
    pickle.dump(representations, f)
    f.close()

    print("Representations stored in ", settings.IMG_DB_PATH, "/", file_name)


class DetectionClientConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'detection_client'

    def ready(self):
        """
        Code exécuté au lancement du serveur
        """
        run_once = os.environ.get('CMDLINERUNNER_RUN_ONCE')

        if run_once is not None:
            return

        os.environ['CMDLINERUNNER_RUN_ONCE'] = 'True'

        # suppression du fichier de bdd d'empreinte des visages s'il existe
        file_name = "representations_%s.pkl" % settings.MODEL_NAME
        file_name = file_name.replace("-", "_").lower()
        img_db_path = os.path.join(settings.IMG_DB_PATH, file_name)
        if os.path.exists(img_db_path):
            os.remove(img_db_path)

        # Et on en reconstruit un. Pour optimisation avec plus de données il faudrait intégrer les nouvelles
        # photos directement dans l'archive pickle
        build_database_file(file_name)
