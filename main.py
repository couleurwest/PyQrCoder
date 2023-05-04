import tkinter.messagebox

import eel
import yaml
from dreamtools import profiler
from validator import validate

from wwwproject.controller.ecarder import ECarder
from wwwproject.controller.ecoder import QRCoder
from wwwproject.controller.validation import URLRule

export = profiler.path_build(profiler.dircurrent(__file__), 'generation')
profiler.makedirs(export)

@eel.expose
def generate_vcard(dts):
    """
    Génération d'un QR Code Carte de visite
    :param dict dts: {nom:required, prenom:required, email:required, phone_1:optional, phone_2:optional, url:optional, corp:optional}
    """
    card = ECarder(**dts)
    qr = QRCoder(export)
    status, message = qr.vcard(card)

    eel.log_result(status, message)


@eel.expose
def generate_url(url):
    """
    Génération d'un QR Code URL
    :param str url: lien site web
    """
    url = url.lower()

    if url:
        result, _, errors = validate({'url': url}, {"url": URLRule()}, return_info=True)  # True

        if result:
            qr = QRCoder(export)
            status, message = qr.uri(url)
        else:
            status, message = "alert", "Génération impossible: URL non valide"
    else:
        status, message = "alert", "Génération impossible: Veuillez saisir une URL"

    eel.log_result(status, message)


def lauch_edge(parametres):
    """
    Lancement de EDGE si pas electron ni chrome-app
    :param dict parametres: Parametres de configuration
    """
    import sys
    import platform

    if sys.platform in ['win32', 'win64'] and int(platform.release()) >= 10:
        eel.start('index.html', **parametres)
    else:
        tkinter.messagebox.showinfo("Erreur : Execution impossible", "Votre environnement n'est pas compatible")


@eel.expose
def exit():
    from sys import exit
    exit(0)


if __name__ == '__main__':
    eel.init('wwwproject', allowed_extensions=['.js', 'html'])
    with open("config.yml", "r") as stream:

        try:
            dcm = yaml.safe_load(stream)
            param = dcm.pop('basis')
        except Exception:
            tkinter.messagebox.showwarning("Erreur : Execution impossible", 'Fichier de configuration manquant')
            dcm = {}

        for mode, mode_param in dcm.items():
            try:
                p = {**param, **mode_param}
                if mode == "edge":
                    lauch_edge(p)
                else:
                    eel.start('index.html', **p)
                break
            except Exception as e:
                pass
