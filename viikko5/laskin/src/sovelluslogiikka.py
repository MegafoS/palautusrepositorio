class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self.muisti = []
    def _talleta(self):
        self.muisti.append(self._arvo)

    def miinus(self, operandi):
        self._talleta()
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self._talleta()
        self._arvo = self._arvo + operandi

    def nollaa(self):
        self._talleta()
        self._arvo = 0

    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def arvo(self):
        return self._arvo
    
    def kumoa(self):
        if self._talleta:
            self._arvo = self.muisti.pop()
