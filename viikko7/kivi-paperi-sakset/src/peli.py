from tuomari import Tuomari

class KiviPaperiSakset:
    def pelaa(self):
        tuomari = Tuomari()
        ekan_siirto = self._ensimmaisen_siirto()
        tokan_siirto = self._toisen_siirto(ekan_siirto)

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)
            ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto = self._toisen_siirto(ekan_siirto)
        print("Kiitos!")
        print(tuomari)
    def _ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")
    # tämän metodin toteutus vaihtelee eri pelityypeissä
    def _toisen_siirto(self, ensimmaisen_siirto):
        # metodin oletustoteutus
        return "k"
    def _onko_ok_siirto(self, siirto):
        return siirto in ["k","s","p"]
    
    def luo_peli(pelityyppi):
        if pelityyppi == "b":
            from kps_tekoaly import KPSTekoaly
            return KPSTekoaly()
        elif pelityyppi == "c":
            from kps_parempi_tekoaly import KPSParempiTekoaly
            return KPSParempiTekoaly()
        else:
            from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
            return KPSPelaajaVsPelaaja()