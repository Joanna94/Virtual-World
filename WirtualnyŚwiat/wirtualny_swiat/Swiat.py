from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import Antylopa
import Czlowiek
import Guarana
import Lis
import Mlecz
import Owca
import Trawa
import WilczeJagody
import Wilk
import Zolw


class Swiat(object):
    __rozmiar = 20
    __rozmiarPola = 20
    __organizmy = []
    __daneZPliku = []
    __okno = Tk()
    __tlo = Canvas(__okno, width = 400, height = 400, bg = "white")
    __tlo.pack(expand = NO, fill = Y)
    __calopalenie = False
    __licznikCalopalenie = 0
    __licznikPrzerwaC = 5
    __czlowiekKierunek = 0
   

    def rysujPoczatek(self):         
        __calopalenie = False
        __licznikCalopalenie = 0
        __licznikPrzerwaC = 5
        __czlowiekKierunek = 0
        print("------------------------NOWY SWIAT------------------------")

        self.pobierzListe().append(Antylopa.Antylopa(5, 5, self))
        self.pobierzListe().append(Antylopa.Antylopa(7, 6, self))
        self.pobierzListe().append(Antylopa.Antylopa(17, 13, self))
        self.pobierzListe().append(Antylopa.Antylopa(1, 2, self))
        self.pobierzListe().append(Czlowiek.Czlowiek(9, 9, self))
        self.pobierzListe().append(Guarana.Guarana(18, 19, self))
        self.pobierzListe().append(Guarana.Guarana(2, 12, self))
        self.pobierzListe().append(Lis.Lis(16, 3, self))
        self.pobierzListe().append(Lis.Lis(14, 7, self))
        self.pobierzListe().append(Lis.Lis(6, 17, self))
        self.pobierzListe().append(Lis.Lis(6, 19, self))
        self.pobierzListe().append(Mlecz.Mlecz(1, 1, self))
        self.pobierzListe().append(Mlecz.Mlecz(15, 15, self))
        self.pobierzListe().append(Owca.Owca(4, 3, self))
        self.pobierzListe().append(Owca.Owca(10, 5, self))
        self.pobierzListe().append(Owca.Owca(5, 1, self))
        self.pobierzListe().append(Owca.Owca(7, 12, self))
        self.pobierzListe().append(Trawa.Trawa(13, 14, self))
        self.pobierzListe().append(Trawa.Trawa(4, 19, self))
        self.pobierzListe().append(WilczeJagody.WilczeJagody(11, 2, self))
        self.pobierzListe().append(WilczeJagody.WilczeJagody(8, 17, self))
        self.pobierzListe().append(Wilk.Wilk(2, 16, self))
        self.pobierzListe().append(Wilk.Wilk(19, 6, self))
        self.pobierzListe().append(Wilk.Wilk(13, 0, self))
        self.pobierzListe().append(Wilk.Wilk(3, 15, self))
        self.pobierzListe().append(Zolw.Zolw(12, 12, self))
        self.pobierzListe().append(Zolw.Zolw(11, 11, self))
        self.pobierzListe().append(Zolw.Zolw(4, 14, self))
        self.pobierzListe().append(Zolw.Zolw(9, 14, self))
        
    def lewo(event):
        Swiat.__czlowiekKierunek = 2
        print("lewo")
    def prawo(event):
        Swiat.__czlowiekKierunek = 1
        print("prawo")
    def gora(event):
        Swiat.__czlowiekKierunek = 4
        print("gora")
    def dol(event):
        Swiat.__czlowiekKierunek = 3
        print("dol")

    __okno.bind("<KeyPress-Up>", gora)
    __okno.bind("<KeyPress-Down>", dol)
    __okno.bind("<KeyPress-Left>", lewo)
    __okno.bind("<KeyPress-Right>", prawo)
    
    def wlaczCalopalenie(self):
        if self.pobierzCzlowiek() != None:
            if self.__licznikPrzerwaC >= 5:
                self.__calopalenie = True
                self.__licznikCalopalenie = 5
                self.__licznikPrzerwaC = 0
                print("Wlaczano calopalenie")
            
        
    def wyswietlLegende(self):
        okno2 = Tk()
        okno2.title("Legenda")
        legenda = Canvas(okno2, width = 300, height = 300, bg = "white")
        legenda.pack(expand = NO, fill = Y)

        org1 = Label(legenda, text = "Człowiek", bg = "black", fg = "white", height = 1, width = 10)
        org2 = Label(legenda, text = "Antylopa", bg = "pink", fg = "black", height = 1, width = 10)
        org3 = Label(legenda, text = "Guarana", bg = "red", fg = "black", height = 1, width = 10)
        org4 = Label(legenda, text = "Lis", bg = "orange", fg = "black", height = 1, width = 10)
        org5 = Label(legenda, text = "Mlecz", bg = "yellow", fg = "black", height = 1, width = 10)
        org6 = Label(legenda, text = "Owca", bg = "cyan", fg = "black", height = 1, width = 10)
        org7 = Label(legenda, text = "Trawa", bg = "green", fg = "black", height = 1, width = 10)
        org8 = Label(legenda, text = "Wilcze jagody", bg = "magenta", fg = "black", height = 1, width = 10)
        org9 = Label(legenda, text = "Wilk", bg = "gray", fg = "black", height = 1, width = 10)
        org10 = Label(legenda, text = "Żółw", bg = "blue", fg = "white", height = 1, width = 10)

        org1.pack(expand=NO, fill=Y, padx = 60)
        org2.pack(expand=NO, fill=Y, padx = 60)
        org3.pack(expand=NO, fill=Y, padx = 60)
        org4.pack(expand=NO, fill=Y, padx = 60)
        org5.pack(expand=NO, fill=Y, padx = 60)
        org6.pack(expand=NO, fill=Y, padx = 60)
        org7.pack(expand=NO, fill=Y, padx = 60)
        org8.pack(expand=NO, fill=Y, padx = 60)
        org9.pack(expand=NO, fill=Y, padx = 60)
        org10.pack(expand=NO, fill=Y, padx = 60)

    
    def nowySwiat(self):
        self.wyczyscSwiat()
        self.__organizmy = []       
        self.rysujPoczatek()
        
    def ustawOkno(self):
        self.__okno.title("Wirtualny Swiat - Joanna Jankowska")
        ramka = Frame(self.__okno)
        tura = Button(ramka, text = "Nowa tura", bg = "pink", command = self.wykonajTure)
        calopalenie = Button(ramka, text = "Calopalenie", bg = "red", command = self.wlaczCalopalenie)
        ramka.pack(side = TOP)
        tura.pack(side = LEFT)
        calopalenie.pack(side = LEFT)
        #menu
        menu = Menu(self.__okno)
        menuplik = Menu(menu)
        menu.add_cascade(label= "Nowy świat", command = self.nowySwiat)
        menu.add_cascade(label = "Zapisz świat", command = self.zapiszSwiat)
        menu.add_cascade(label = "Wczytaj świat", command = self.wczytajSwiat)
        menu.add_cascade(label = "Legenda", command = self.wyswietlLegende)
        self.__okno.config(menu=menu)

        self.__okno.mainloop(); #to musi byc ostatnie
    
    def pobierzCzlowiek(self):
        for organizm in self.__organizmy:
            if organizm.imie == "Czlowiek":
                return organizm
        return None
        
    def wykonajTure(self): #tura
        self.sortujOrganizmy()

        for reset in self.__organizmy:
            reset.juzByl = False
        
        print("KOLEJNA TURA")

        for organizm in self.__organizmy:
            if organizm.juzByl == False:
                organizm.akcja(self)
                organizm.juzByl = True
            if self.pobierzCzlowiek() != None:
                if self.__calopalenie == True:
                    self.pobierzCzlowiek().calopalenie(self)

        if self.__calopalenie == True:
            self.__licznikCalopalenie = self.__licznikCalopalenie - 1  #odliczam ile razy uzytko calopalenia
            print("Calopalenie - ilosc tur do wylaczenia:", self.__licznikCalopalenie)
            if self.__licznikCalopalenie == 0:
                self.__calopalenie = False #jesli uzyto 5 razy, to ustawiam zmienna na false by "wylaczyc" skilla

        if self.__calopalenie == False:
            self.__licznikPrzerwaC = self.__licznikPrzerwaC + 1

        self.rysujSwiat()

    def sortujOrganizmy(self): #sortowanie
        for i in range(self.getIloscOrganizmow() - 1, 0, -1):
            for j in range(i):
                if self.__organizmy[j].inicjatywa < self.__organizmy[j + 1].inicjatywa:
                    self.swap(self.__organizmy, j)
                elif self.__organizmy[j].inicjatywa == self.__organizmy[j + 1].inicjatywa:
                    if self.__organizmy[j].czasZycia < self.__organizmy[j + 1].czasZycia:
                        self.swap(self.__organizmy, j)
        
    def swap(self, org, j):
        org[j], org[j + 1] = org[j + 1], org[j]
        
    def wyczyscSwiat(self):
        for wsp_y in range (self.__rozmiar):
            for wsp_x in range (self.__rozmiar):
                self.usunOrganizmNaPozycji(wsp_x, wsp_y)

    def rysujSwiat(self):
        self.wyczyscSwiat()
        for doNarysowania in self.__organizmy:
            doNarysowania.rysujOrganizm(self.__tlo, doNarysowania.imie, doNarysowania.x, doNarysowania.y)
            
        
    def czyZajete(self, wsp_x, wsp_y):
        for zajete in self.__organizmy:
            if zajete.x == wsp_x and zajete.y == wsp_y:
                return zajete
        return None

       
    def usunOrganizmNaPozycji(self, wsp_x, wsp_y):
        kwadrat = self.__tlo.create_rectangle(20*wsp_x+2, 20*wsp_y+2, 20*(wsp_x+1), 20*(wsp_y+1), fill = "white", outline = "white")

    def usunOrganizmZeSwiata(self, wsp_x, wsp_y):
        doUsuniecia = self.czyZajete(wsp_x, wsp_y)

        if doUsuniecia != None:
            self.__organizmy.remove(doUsuniecia)

    def getRozmiar(self):
        return self.__rozmiar

    def getTlo(self):
        return self.__tlo

    def pobierzListe(self):
        return self.__organizmy

    def getIloscOrganizmow(self):
        return self.__organizmy.__len__()

    def getKierunek(self):
        return self.__czlowiekKierunek

    def zapiszSwiat(self):
        nazwa = None
        dlg = filedialog.SaveAs(initialfile = nazwa)
        plik = dlg.show()

        if len(plik):
            nazwa = plik
            if nazwa:
                plik = open(nazwa + ".txt", 'w')
        
                for org in self.__organizmy:
                    plik.write(org.imie + ' ' + str(org.x) + ' ' + str(org. y) + '\n')
                plik.close()

    def wczytajSwiat(self):
        nazwa = None
        self.__daneZPliku = []
        dlg = filedialog.Open(initialfile = nazwa)
        plik = dlg.show()
        wczytano = False

        if len(plik):
            nazwa = plik
            with open(nazwa, 'r') as plik:
                for linia in plik.readlines():
                    czesci = linia.split(' ')

                    if czesci.__len__() != 3:
                        messagebox.showinfo("Blad!", "Niewlasciwy plik!")
                        wczytano = False
                    else:
                        imie = czesci[0]
                        wsp_x = czesci[1]
                        wsp_y = czesci[2]

                        self.__daneZPliku.append(imie)
                        self.__daneZPliku.append(wsp_x)
                        self.__daneZPliku.append(wsp_y)
                        wczytano = True

            if wczytano == True:
                self.wczytanySwiat()



    def wczytanySwiat(self):
        self.wyczyscSwiat()
        self.__organizmy = []
        __calopalenie = False
        __licznikCalopalenie = 0
        __licznikPrzerwaC = 5
        __czlowiekKierunek = 0
        print("------------------------WCZYTANY SWIAT------------------------")

        for i in range(self.__daneZPliku.__len__()):
            if i % 3 == 0:
                imie = self.__daneZPliku[i]
                wsp_x = int(self.__daneZPliku[i + 1])
                wsp_y = int(self.__daneZPliku[i + 2])

                if imie == "Antylopa" : self.pobierzListe().append(Antylopa.Antylopa(wsp_x, wsp_y, self))
                elif imie == "Czlowiek": self.pobierzListe().append(Czlowiek.Czlowiek(wsp_x, wsp_y, self))
                elif imie == "Guarana": self.pobierzListe().append(Guarana.Guarana(wsp_x, wsp_y, self))
                elif imie == "Lis": self.pobierzListe().append(Lis.Lis(wsp_x, wsp_y, self))
                elif imie == "Mlecz": self.pobierzListe().append(Mlecz.Mlecz(wsp_x, wsp_y, self))
                elif imie == "Owca": self.pobierzListe().append(Owca.Owca(wsp_x, wsp_y, self))
                elif imie == "Trawa": self.pobierzListe().append(Trawa.Trawa(wsp_x, wsp_y, self))
                elif imie == "WilczeJagody": self.pobierzListe().append(WilczeJagody.WilczeJagody(wsp_x, wsp_y, self))
                elif imie == "Wilk": self.pobierzListe().append(Wilk.Wilk(wsp_x, wsp_y, self))
                elif imie == "Zolw": self.pobierzListe().append(Zolw.Zolw(wsp_x, wsp_y, self))

