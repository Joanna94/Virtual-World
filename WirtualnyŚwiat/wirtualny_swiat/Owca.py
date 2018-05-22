from Zwierze import *

class Owca(Zwierze):
    def __init__(self, wsp_x, wsp_y, swiat):
        self.imie = "Owca"
        self.sila = 0
        self.inicjatywa = 4
        self.czasZycia = 4
        self.x = wsp_x
        self.y = wsp_y
        self.rysujOrganizm(swiat.getTlo(), self.imie, self.x, self.y)
        self.juzByl = False
        self.kierunek = 0

    def rozmnoz(self, wsp_x, wsp_y, swiat):
        swiat.pobierzListe().append(Owca(wsp_x, wsp_x, swiat))
