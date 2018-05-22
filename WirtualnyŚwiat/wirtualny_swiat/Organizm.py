from Swiat import *
from tkinter import *

class Organizm(object):

    def akcja(self, swiat):
        pass

    def kolizja(self, swiat, wsp_x, wsp_y):
        pass
    @property
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y
    @property
    def imie(self):
        return self.__imie
    @property
    def inicjatywa(self):
        return self.__inicjatywa
    @property
    def sila(self):
        return self.__sila
    @property
    def czasZycia(self):
        return self.__czasZycia
    @property
    def juzByl(self):
        return self.__juzByl
    @property
    def kierunek(self):
        return self.__kierunek
    @x.setter
    def x(self, x):
        self.__x = x
    @y.setter
    def y(self, y):
        self.__y = y
    @sila.setter
    def sila(self, sila):
        self.__sila = sila
    @czasZycia.setter
    def czasZycia(self, czasZycia):
        self.__czasZycia = czasZycia
    @imie.setter
    def imie(self, imie):
        self.__imie = imie
    @inicjatywa.setter
    def inicjatywa(self, inicjatywa):
        self.__inicjatywa = inicjatywa
    @juzByl.setter
    def juzByl(self, byl):
        self.__juzByl = byl
    @kierunek.setter
    def kierunek(self, kierunek):
        self.__kierunek = kierunek

    def rysujOrganizm(self, kontener, imie, wsp_x, wsp_y):
        kolor = ""
        if imie == "Czlowiek": kolor = "black"
        if imie == "Antylopa": kolor = "pink"
        if imie == "Guarana": kolor = "red"
        if imie == "Lis": kolor = "orange"
        if imie == "Mlecz": kolor = "yellow"
        if imie == "Owca": kolor = "cyan"
        if imie == "Trawa": kolor = "green"
        if imie == "WilczeJagody": kolor = "magenta"
        if imie == "Wilk": kolor = "gray"
        if imie == "Zolw": kolor = "blue"

        if imie == "Czlowiek":
            kwadrat = kontener.create_rectangle(20*wsp_x+2, 20*wsp_y+2, 20*(wsp_x+1), 20*(wsp_y+1), fill = kolor, outline = "magenta")
        else:
            kwadrat = kontener.create_rectangle(20*wsp_x+2, 20*wsp_y+2, 20*(wsp_x+1), 20*(wsp_y+1), fill = kolor)