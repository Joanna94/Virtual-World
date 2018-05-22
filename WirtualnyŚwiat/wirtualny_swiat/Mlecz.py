from Roslina import *

class Mlecz(Roslina):
    def __init__(self, wsp_x, wsp_y, swiat):
        self.imie = "Mlecz"
        self.sila = 0
        self.inicjatywa = 0
        self.czasZycia = 0
        self.x = wsp_x
        self.y = wsp_y
        self.rysujOrganizm(swiat.getTlo(), self.imie, self.x, self.y)
        self.juzByl = False
        self.kierunek = 0

    def rozsiej(self, wsp_x, wsp_y, swiat):
        swiat.pobierzListe().append(Mlecz(wsp_x, wsp_y, swiat))

    def akcja(self, swiat):
        for proba in range(3):
            super(Mlecz, self).akcja(swiat)