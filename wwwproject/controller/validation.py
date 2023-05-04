import re

from validator.rules_src import Rule

from wwwproject.controller.toolbox import RGX_PHONE, RGX_URL, RGX_EMAIL


class PhoneRule(Rule):
    regex = re.compile(RGX_PHONE)  # chaines commençant par b ou B

    def __init__(self):
        super(PhoneRule, self).__init__()
        self.error_message = "Téléphone non valide"

    def check(self, txt):
        if txt:
            return self.regex.match(txt) is not None
        return True


class URLRule(Rule):
    regex = re.compile(RGX_URL)

    def __init__(self):
        super(URLRule, self).__init__()
        self.error_message = "URL non valide"

    def check(self, txt):
        if txt:
            return self.regex.match(txt) is not None
        else:
            return True


class EMAILRule(Rule):
    regex = re.compile(RGX_EMAIL)

    def __init__(self, required=False):
        super(EMAILRule, self).__init__()

        self.error_message = "Courriel non valide"
        self.required = required

    def check(self, txt):
        if txt:
            return self.regex.match(txt) is not None
        elif self.required:
            self.error_message = "Courriel manquant"
            return False
        else:
            return True
