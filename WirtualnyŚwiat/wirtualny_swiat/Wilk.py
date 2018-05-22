from Zwierze import *

class Wilk(Zwierze):
    def __init__(self, wsp_x, wsp_y, swiat):
        self.imie = "Wilk"
        self.sila = 9
        self.inicjatywa = 5
        self.czasZycia = 0
        self.x = wsp_x
        self.y = wsp_y
        self.rysujOrganizm(swiat.getTlo(), self.imie, self.x, self.y)
        self.juzByl = False
        self.kierunek = 0

    def rozmnoz(self, wsp_x, wsp_y, swiat):
        swiat.pobierzListe().append(Wilk(wsp_x, wsp_x, swiat))
