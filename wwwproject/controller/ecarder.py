import dataclasses

from dreamtools.tools import clean_space


@dataclasses.dataclass
class ECarder:
    name: str
    surname: str
    email: str

    phone_1: str = ""
    phone_2: str = ""

    url: str = ""
    corp: str = ""

    @property
    def card_name(self):
        """Mise en forme identité"""
        if self.name and self.surname:
            return self.name.upper() + ',' + self.surname.capitalize()
        else:
            return self.name or self.surname
    @property
    def card_phone(self):
        return list(map(lambda d: clean_space(d), filter(lambda d: d, [self.phone_1, self.phone_2])))

    @property
    def mecard_data(self):
        """Donnes au format MeCard"""
        dcm = {
            'email': self.email,
            'nickname': self.corp,
            'url': self.url,
            'phone': self.card_phone,
            'name': self.card_name,
        }
        return {k: v for (k, v) in dcm.items() if v}

    @property
    def mecard(self):
        """schement de validation """
        dcm = {
            'name': self.name,
            'surname': self.surname,
            'email': self.email,
            'phone_1': self.phone_1,
            'corp': self.corp,
            'url': self.url,
            'phone_2': self.phone_2,
        }
        return {k: v or '' for (k, v) in dcm.items()}

