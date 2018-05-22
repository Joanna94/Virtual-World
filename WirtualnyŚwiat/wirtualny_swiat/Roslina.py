import random;
from Organizm import *

class Roslina(Organizm):
    def akcja(self, swiat):
        prawdopodobienstwo = random.randint(0,10)

        if prawdopodobienstwo == 1:
            kierunek = random.randint(1,4)

            wsp_x = self.x
            wsp_y = self.y

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

            inny = swiat.czyZajete(wsp_x, wsp_y)

            if  inny == None:
                self.rozsiej(wsp_x, wsp_y, swiat)



