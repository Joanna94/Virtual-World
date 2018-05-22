from Zwierze import *
import random

class Lis(Zwierze):
    def __init__(self, wsp_x, wsp_y, swiat):
        self.imie = "Lis"
        self.sila = 3
        self.inicjatywa = 7
        self.czasZycia = 0
        self.x = wsp_x
        self.y = wsp_y
        self.rysujOrganizm(swiat.getTlo(), self.imie, self.x, self.y)
        self.juzByl = False
        self.kierunek = 0

    def rozmnoz(self, wsp_x, wsp_y, swiat):
        swiat.pobierzListe().append(Lis(wsp_x, wsp_x, swiat))

    def akcja(self, swiat):
        self.czasZycia = self.czasZycia + 1

        wsp_x = self.x
        wsp_y = self.y
        kierunek = random.randint(1,4)

        if kierunek == 1:
            wsp_x = wsp_x + 1
        elif kierunek == 2:
            wsp_x = wsp_x - 1
        elif kierunek == 3:
            wsp_y = wsp_y + 1
        elif kierunek == 4:
            wsp_y = wsp_y - 1

        if wsp_x < 0 or wsp_x > swiat.getRozmiar() - 1 or wsp_y < 0 or wsp_y > swiat.getRozmiar() - 1:
            return

        self.kierunek = kierunek

        inny = swiat.czyZajete(wsp_x, wsp_y)
        if inny == None:
            self.x = wsp_x
            self.y = wsp_y
        elif inny.sila > self.sila: #nie ruszy sie na pole zajmowane przez organizm silniejszy niz on
            print("Dobry wech ", self.imie, ", inny organizm: ", inny.imie, " (", self.x, ",", self.y, ")", sep = '') 
        else:
            super(Lis, self).kolizja(swiat, wsp_x, wsp_y)


