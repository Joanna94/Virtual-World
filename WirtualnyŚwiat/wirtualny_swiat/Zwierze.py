from Organizm import *
import random

class Zwierze(Organizm):
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

        if swiat.czyZajete(wsp_x, wsp_y) == None:
            self.x = wsp_x
            self.y = wsp_y
        else:
            self.kolizja(swiat, wsp_x, wsp_y)

    def kolizja(self, swiat, wsp_x, wsp_y):
       inny = swiat.czyZajete(wsp_x, wsp_y)
       miejsce = None

       if self.imie == inny.imie:
            miejsce = False
            r_x = 0
            r_y = 0

            if wsp_x + 1 < swiat.getRozmiar():
                inny = swiat.czyZajete(wsp_x + 1, wsp_y)
                if inny == None:
                    miejsce = True
                    r_x = wsp_x + 1
                    r_y = wsp_y
            elif wsp_x - 1 >= 0:
                inny = swiat.czyZajete(wsp_x - 1, wsp_y)
                if inny == None:
                    miejsce = True;
                    r_x = wsp_x - 1
                    r_y = wsp_y
            elif wsp_y + 1 < swiat.getRozmiar():
                inny = swiat.czyZajete(wsp_x, wsp_y + 1)
                if inny == None:
                    miejsce = True
                    r_x = wsp_x
                    r_y = wsp_y + 1
            elif wsp_y - 1 >= 0:
                inny = swiat.czyZajete(wsp_x, wsp_y - 1)
                if inny == None:
                    miejsce = True;
                    r_x = wsp_x
                    r_y = wsp_y - 1
            elif wsp_x + 1 < swiat.getRozmiar() and wsp_y + 1 < swiat.getRozmiar():
                inny = swiat.czyZajete(wsp_x + 1, wsp_y + 1)
                if inny == None:
                    miejsce = True
                    r_x = wsp_x + 1
                    r_y = wsp_y + 1
            elif wsp_x - 1 >= 0 and wsp_y >= 0:
                inny = swiat.czyZajete(wsp_x - 1, wsp_y - 1)
                if inny == None:
                    miejsce = True
                    r_x = wsp_x - 1
                    r_y = wsp_y - 1
            elif wsp_x + 1 < swiat.getRozmiar() and wsp_y - 1 >= 0:
                inny = swiat.czyZajete(wsp_x + 1, wsp_y - 1)
                if inny == None:
                    miejsce = True
                    r_x = wsp_x + 1
                    r_y = wsp_y - 1
            elif wsp_x - 1 >= 0 and wsp_y + 1 < swiat.getRozmiar():
                inny = swiat.czyZajete(wsp_x - 1, wsp_y + 1)
                if inny == None:
                    miejsce = True
                    r_x = wsp_x - 1
                    r_y = wsp_y + 1
            
            if miejsce == True:
                self.rozmnoz(r_x, r_y, swiat)
                print("Urodzil sie ", self.imie, " (", self.x, ",", self.y, ")", sep = '')
       else:
            if inny.imie == "Guarana":
                swiat.usunOrganizmZeSwiata(inny.x, inny.y)
                swiat.usunOrganizmNaPozycji(inny.x, inny.y)                
                self.sila = self.sila + 3
                self.x = wsp_x
                self.y = wsp_y
                print(self.imie, " zjadl ", inny.imie, " i ma teraz ", self.sila, " sily (", self.x, ",", self.y, ")", sep = '')
            elif inny.imie == "WilczeJagody":
                swiat.usunOrganizmZeSwiata(self.x, self.y)
                swiat.usunOrganizmNaPozycji(self.x, self.y)
                swiat.usunOrganizmZeSwiata(inny.x, inny.y)
                swiat.usunOrganizmNaPozycji(inny.x, inny.y) 
                print(self.imie, " zjadl ", inny.imie, " i zginal (", self.x, ",", self.y, ")", sep = '')
            elif inny.imie == "Zolw": #kolizja zolw
                if self.sila < 5:
                    print(inny.imie, " odparl atak ", self.imie, " (", self.x, ",", self.y, ")", sep = '')          
            else:
                if self.sila >= inny.sila:
                    swiat.usunOrganizmZeSwiata(inny.x, inny.y)
                    swiat.usunOrganizmNaPozycji(inny.x, inny.y)
                    self.x = wsp_x
                    self.y = wsp_y
                    print(self.imie, " zabil ", inny.imie, " (", self.x, ",", self.y, ")", sep = '')
                elif self.sila < inny.sila:
                    swiat.usunOrganizmZeSwiata(self.x, self.y)
                    swiat.usunOrganizmNaPozycji(self.x, self.y)
                    inny.x = wsp_x
                    inny.y = wsp_y
                    print(inny.imie, " zabil ", self.imie, " (", self.x, ",", self.y, ")", sep = '')
                


