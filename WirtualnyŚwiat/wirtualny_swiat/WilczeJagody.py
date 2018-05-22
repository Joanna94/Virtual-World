from Roslina import *

class WilczeJagody(Roslina):
    def __init__(self, wsp_x, wsp_y, swiat):
        self.imie = "WilczeJagody"
        self.sila = 99
        self.inicjatywa = 0
        self.czasZycia = 0
        self.x = wsp_x
        self.y = wsp_y
        self.rysujOrganizm(swiat.getTlo(), self.imie, self.x, self.y)
        self.juzByl = False
        self.kierunek = 0

    def rozsiej(self, wsp_x, wsp_y, swiat):
        swiat.pobierzListe().append(WilczeJagody(wsp_x, wsp_y, swiat))