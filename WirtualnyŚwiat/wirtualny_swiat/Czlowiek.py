from Zwierze import *

class Czlowiek(Zwierze):
    def __init__(self, wsp_x, wsp_y, swiat):
        self.imie = "Czlowiek"
        self.sila = 5
        self.inicjatywa = 4
        self.czasZycia = 0
        self.x = wsp_x
        self.y = wsp_y
        self.rysujOrganizm(swiat.getTlo(), self.imie, self.x, self.y)
        self.juzByl = False
        self.kierunek = 0

    def rozmnoz(self, wsp_x, wsp_y, swiat):
        pass

    def akcja(self, swiat):
        self.czasZycia = self.czasZycia + 1
        self.kierunek = swiat.getKierunek()

        wsp_x = self.x
        wsp_y = self.y

        if self.kierunek == 1: #prawo
            wsp_x = wsp_x + 1
        elif self.kierunek == 2: #lewo
            wsp_x = wsp_x - 1
        elif self.kierunek == 3: #dol
            wsp_y = wsp_y + 1
        elif self.kierunek == 4: #gora
            wsp_y = wsp_y - 1

        if wsp_x < 0 or wsp_x > swiat.getRozmiar() - 1 or wsp_y < 0 or wsp_y > swiat.getRozmiar() - 1:
            return

        
        if swiat.czyZajete(wsp_x, wsp_y) == None:
            self.x = wsp_x
            self.y = wsp_y
        else:
            self.kolizja(swiat, wsp_x, wsp_y)
    
    def calopalenie(self, swiat):

        wsp_x = self.x
        wsp_y = self.y        
        
        if wsp_x < swiat.getRozmiar() - 2:
            inny = swiat.czyZajete(wsp_x + 1, wsp_y)                
            swiat.usunOrganizmNaPozycji(wsp_x + 1, wsp_y)
            swiat.usunOrganizmZeSwiata(wsp_x + 1, wsp_y)                
            if  inny != None:
                print(self.imie, " zmiotl ", inny.imie, " (", inny.x, ",", inny.y, ")", sep = '')
        if wsp_x > 0:
            inny = swiat.czyZajete(wsp_x - 1, wsp_y)
            swiat.usunOrganizmNaPozycji(wsp_x - 1, wsp_y)
            swiat.usunOrganizmZeSwiata(wsp_x - 1, wsp_y)
            if inny != None:
                print(self.imie, " zmiotl ", inny.imie, " (", inny.x, ",", inny.y, ")", sep = '')
        if wsp_y > 0:
            inny = swiat.czyZajete(wsp_x, wsp_y - 1)                
            swiat.usunOrganizmNaPozycji(wsp_x, wsp_y - 1)
            swiat.usunOrganizmZeSwiata(wsp_x, wsp_y - 1)
            if inny != None:
                print(self.imie, " zmiotl ", inny.imie, " (", inny.x, ",", inny.y, ")", sep = '')
        if wsp_y < swiat.getRozmiar() - 2:
            inny = swiat.czyZajete(wsp_x, wsp_y + 1)
            swiat.usunOrganizmNaPozycji(wsp_x, wsp_y + 1)
            swiat.usunOrganizmZeSwiata(wsp_x, wsp_y + 1)
            if inny != None:
                print(self.imie, " zmiotl ", inny.imie, " (", inny.x, ",", inny.y, ")", sep = '')

    def kolizja(self, swiat, wsp_x, wsp_y):
        inny = swiat.czyZajete(wsp_x, wsp_y)

        if self.imie == inny.imie:
            pass
        else:
            super(Czlowiek, self).kolizja(swiat, wsp_x, wsp_y)