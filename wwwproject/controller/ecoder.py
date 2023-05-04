import eel
import qrcode
from PIL import Image
from dreamtools import profiler
from validator import validate

from wwwproject.controller import QRcolor
from wwwproject.controller.validation import URLRule, PhoneRule, EMAILRule


class QRCoder():
    logo = profiler.path_build(profiler.dircurrent(__file__), '../pics/logo.jpg')

    def __init__(self, export, **kw):
        super(QRCoder, self).__init__(**kw)
        self.export = export

    def vcard(self, card):
        from segno import helpers

        dcm = card.mecard

        if dcm:
            result, _, errors = validate(dcm, self.card_rules, return_info=True)  # True

            if result:
                qrcode = helpers.make_mecard(**card.mecard_data)
                path_export = profiler.path_build(self.export, 'qrcode_vcard.png')
                qrcode.save(path_export, dark=QRcolor, scale=4)
                return "success", f"QRCode generated : {profiler.path_build(self.export, 'qrcode_vcard.png')}"
            else:
                for field, err in errors.items():
                    eel.set_backround(field, False)

                return "alert", "Génération impossible: Vérifier les données saisie"

        return "alert", "Génération impossible: Renseignez le formulaire"

    def uri(self, url):
        """Generation d'un QRCode pour URL"""
        try:
            path_export = profiler.path_build(self.export, 'qrcode_uri.png')
            logo = Image.open(self.logo)

            basewidth = 100

            # adjust image size
            wpercent = (basewidth / float(logo.size[0]))
            hsize = int((float(logo.size[1]) * float(wpercent)))

            logo = logo.resize((basewidth, hsize), Image.Resampling.LANCZOS)

            QRcode = qrcode.QRCode(
                error_correction=qrcode.constants.ERROR_CORRECT_H
            )

            # adding URL or text to QRcode
            QRcode.add_data(url)

            # generating QR code
            QRcode.make()

            # taking color name from user

            # adding color to QR code
            QRimg = QRcode.make_image(fill_color=QRcolor, back_color="white").convert('RGB')

            # set size of QR code
            pos = ((QRimg.size[0] - logo.size[0]) // 2, (QRimg.size[1] - logo.size[1]) // 2)
            QRimg.paste(logo, pos)

            # save the QR code generated
            QRimg.save(path_export)

            return "success", f"QRCode generated : {path_export}"
        except Exception as e:
            return "alert", f"Erreur systeme: {e.__str__()}"

    def reset_form(self):
        eel.reset_form_js()

    @property
    def card_rules(self):
        return {
            "name": "required",
            "surname": "required",
            "email": EMAILRule(True),
            "url": URLRule(),
            "phone_1": PhoneRule(),
            "phone_2": PhoneRule()
        }
