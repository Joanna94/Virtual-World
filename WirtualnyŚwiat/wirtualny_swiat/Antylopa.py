from Zwierze import *
import random

class Antylopa(Zwierze):
    def __init__(self, wsp_x, wsp_y, swiat):
        self.imie = "Antylopa"
        self.sila = 4
        self.inicjatywa = 4
        self.czasZycia = 0
        self.x = wsp_x
        self.y = wsp_y
        self.rysujOrganizm(swiat.getTlo(), self.imie, self.x, self.y)
        self.juzByl = False
        self.kierunek = 0

    def rozmnoz(self, wsp_x, wsp_y, swiat):
        swiat.pobierzListe().append(Antylopa(wsp_x, wsp_x, swiat))

    def akcja(self, swiat):
        self.czasZycia = self.czasZycia + 1

        wsp_x = self.x
        wsp_y = self.y
        kierunek = random.randint(1,4)

        if kierunek == 1:
            wsp_x = wsp_x + 2
        elif kierunek == 2:
            wsp_x = wsp_x - 2
        elif kierunek == 3:
            wsp_y = wsp_y + 2
        elif kierunek == 4:
            wsp_y = wsp_y - 2

        if wsp_x < 0 or wsp_x > swiat.getRozmiar() - 1 or wsp_y < 0 or wsp_y > swiat.getRozmiar() - 1:
            return

        self.kierunek = kierunek

        if swiat.czyZajete(wsp_x, wsp_y) == None:
            self.x = wsp_x
            self.y = wsp_y
        else:
            self.kolizja(swiat, wsp_x, wsp_y)

    def kolizja(self, swiat, wsp_x, wsp_y):
        inny = swiat.czyZajete(wsp_x, wsp_y)

        if self.imie == inny.imie:
            super(Antylopa, self).kolizja(swiat, wsp_x, wsp_y)
        else:
            if inny.inicjatywa > 0: #tylko zwierzeta
                czyWalka = random.randint(1,2)
                if czyWalka == 1: #walka
                    super(Antylopa, self).kolizja(swiat, wsp_x, wsp_y)
                    print(self.imie, " bierze udzial w walce z ", inny.imie, " (", self.x, ",", self.y, ")", sep = '') 
                elif czyWalka == 2: #ucieczka przed walka
                    miejsce = False
                    m_x = 0
                    m_y = 0

                    if wsp_x + 1 < swiat.getRozmiar():
                        if swiat.czyZajete(wsp_x + 1, wsp_y) == None:
                            miejsce = True
                            m_x = wsp_x + 1
                            m_y = wsp_y
                    elif wsp_x - 1 >= 0:
                        if swiat.czyZajete(wsp_x - 1, wsp_y) == None:
                            miejsce = True
                            m_x = wsp_x - 1
                            m_y = wsp_y
                    elif wsp_y + 1 < swiat.getRozmiar():
                        if swiat.czyZajete(wsp_x, wsp_y + 1) == None:
                            miejsce = True
                            m_x = wsp_x
                            m_y = wsp_y + 1
                    elif wsp_y - 1 >= 0:
                        if swiat.czyZajete(wsp_x, wsp_y - 1) == None:
                            miejsce = True
                            m_x = wsp_x
                            m_y = wsp_y - 1
                    elif wsp_x + 1 < swiat.getRozmiar() and wsp_y + 1 < swiat.getRozmiar():
                        if swiat.czyZajete(wsp_x + 1, wsp_y + 1) == None:
                            miejsce = True
                            m_x = wsp_x + 1
                            m_y = wsp_y + 1
                    elif wsp_x - 1 < swiat.getRozmiar() and wsp_y - 1 < swiat.getRozmiar():
                        if swiat.czyZajete(wsp_x - 1, wsp_y - 1) == None:
                            miejsce = True
                            m_x = wsp_x - 1
                            m_y = wsp_y - 1
                    elif wsp_x + 1 >= 0 and wsp_y - 1 < swiat.getRozmiar():
                        if swiat.czyZajete(wsp_x + 1, wsp_y - 1) == None:
                            miejsce = True
                            m_x = wsp_x + 1
                            m_y = wsp_y - 1
                    elif wsp_x - 1 >= 0 and wsp_y + 1 < swiat.getRozmiar():
                        if swiat.czyZajete(wsp_x - 1, wsp_y + 1) == None:
                            miejsce = True
                            m_x = wsp_x - 1
                            m_y = wsp_y + 1
                
                    if miejsce == True:
                        self.x = m_x
                        self.y = m_y
                        print(self.imie, " uciekla przed walka z ", inny.imie, " (", self.x, ",", self.y, ")", sep = '') 