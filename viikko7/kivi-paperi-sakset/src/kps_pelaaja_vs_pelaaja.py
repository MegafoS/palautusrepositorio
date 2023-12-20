from kps import KiviPaperiSakset

class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def _ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")
    def _toisen_siirto(self, ensimmaisen_siirto):
        return input("Toisen pelaajan siirto: ")