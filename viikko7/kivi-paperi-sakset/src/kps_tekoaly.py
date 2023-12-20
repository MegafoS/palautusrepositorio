from kps import KiviPaperiSakset
from tekoaly import Tekoaly

class KPSTekoaly(KiviPaperiSakset):
    def __init__(self):
        self.tekoaly = Tekoaly()
        self.ekan_siirto = None

    def _ensimmaisen_siirto(self):
        self.ekan_siirto = super()._ensimmaisen_siirto()
        return self.ekan_siirto

    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        self.tekoaly.aseta_siirto(ensimmaisen_siirto)
        return tokan_siirto