"""
Module qui permet de journaliser les erreurs de requêtes
"""
from datetime import date, datetime
import os


def log_error(url, typeReq, code, error):
    today = date.today()
    d1 = today.strftime("%Y%m%d")
    fic_name = "employes/log/log_" + d1 + ".csv"
    entete = False if os.path.exists(fic_name) else True
    with open(fic_name, "a+") as f:
        if entete:
            line = "heure;URL;type;code;message\n"
            f.write(line)

        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        line = time + ";" + url + ";" + typeReq + ";" + str(code) + ";" + error + "\n"
        f.write(line)
