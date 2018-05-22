from Zwierze import *
import random

class Zolw(Zwierze):
    def __init__(self, wsp_x, wsp_y, swiat):
        self.imie = "Zolw"
        self.sila = 2
        self.inicjatywa = 1
        self.czasZycia = 0
        self.x = wsp_x
        self.y = wsp_y
        self.rysujOrganizm(swiat.getTlo(), self.imie, self.x, self.y)
        self.juzByl = False
        self.kierunek = 0

    def rozmnoz(self, wsp_x, wsp_y, swiat):
        swiat.pobierzListe().append(Zolw(wsp_x, wsp_x, swiat))

    def akcja(self, swiat):
        zmianaPolozenia = random.randint(0, 100)

        if zmianaPolozenia < 15: #zolw zmienia swoje polozenie
            super(Zolw, self).akcja(swiat)
        else:
            self.czasZycia = self.czasZycia + 1
            

