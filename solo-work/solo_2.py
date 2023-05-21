class Trojkat:

    def __init__(self, a, b, c, h_a):
        self.a = a
        self.b = b
        self.c = c
        self.h_a = h_a
    # self.obwod = a + b + c

# new
    def obwod(self):
        return self.a + self.b + self.c
    def pole(self):
        return ((self.a * self.h_a) / 2)


class Prostokat:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def obwod(self):
        return 2 * self.a + 2 * self.b
    def pole(self):
        return (self.a * self.b)

trojkat_rownoboczny = Trojkat(10, 10, 10, 8)
moj_trojkat = Trojkat(15, 4, 6, 10)
print(trojkat_rownoboczny.obwod())
print(trojkat_rownoboczny.pole())
print(moj_trojkat.obwod())
print(moj_trojkat.pole())
prostokąt = Prostokat(10, 5)
print(prostokąt.obwod())
print(prostokąt.pole())

#new
class Student:
    def __init__(self, imie, nazwisko, numer_indeksu):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_indeksu = numer_indeksu
        self.oceny = []


    def __str__(self):
        return self.imie + " " + self.nazwisko


    def __int__(self):
        return 5

    def dodaj_ocene(self, ocena):
        self.oceny.append(ocena)

    def zwroc_srednia(self):
        return sum(self.oceny) / len(self.oceny)

student_krzysztof = Student("Krzysztof", "Szczęsny", 129115)
student_krzysztof.dodaj_ocene(4.5)
student_krzysztof.dodaj_ocene(5)
print(student_krzysztof)

class Rower:
    def __init__(self, marka, przeznaczenie, rodzaj_opon, rozmiar, material, amortyzacja, przerzutki, hamulce):
        self.marka = marka
        self.przeznaczenie = przeznaczenie
        self.rodzaj_opon = rodzaj_opon
        self.rozmiar = rozmiar
        self.material = material
        self.amortyzacja = amortyzacja
        self.przerzutki = przerzutki
        self.hamulce = hamulce

    def obliczanie_ceny(self):
        cena = 0
        if self.marka == "cross":
            cena += 1000
        elif self.marka == "giant":
            cena += 700
        elif self.marka == "decathlon":
            cena += 500

        if self.przeznaczenie == "szosowy":
            cena += 300
        elif self.przeznaczenie == "gorski":
            cena += 200
        elif self.przeznaczenie == "miejski":
            cena += 100

        if self.rodzaj_opon == "szosowe":
            cena += 300
        elif self.rodzaj_opon == "gorskie":
            cena += 200
        elif self.rodzaj_opon == "miejskie":
            cena += 100

        if self.rozmiar == "niemowlęce":
            cena += 100
        elif self.rozmiar == "młodziezowe":
            cena += 200
        elif self.rozmiar == "dorosle":
            cena += 500

        if self.material == "carbon":
            cena += 1000
        elif self.material == "stal":
            cena += 500
        elif self.material == "aluminium":
            cena += 700

        if self.amortyzacja == "bdb":
            cena += 500
        elif self.amortyzacja == "db":
            cena += 350
        elif self.amortyzacja == "dst":
            cena += 200

        if self.przerzutki == "12":
            cena += 500
        elif self.przerzutki == "9":
            cena += 300
        elif self.przerzutki == "7":
            cena += 200

        if self.hamulce == "tarczowe":
            cena += 800
        elif self.hamulce == "hydrauliczne":
            cena += 600
        elif self.hamulce == "rolkowe":
            cena += 400

        return cena

    def v_max(self):
        predkosc = 0
        if self.marka == "cross":
            predkosc += 10
        elif self.marka == "giant":
            predkosc += 7
        elif self.marka == "decathlon":
            predkosc += 5

        if self.przeznaczenie == "szosowy":
            predkosc += 3
        elif self.przeznaczenie == "gorski":
            predkosc += 1
        elif self.przeznaczenie == "miejski":
            predkosc += 2

        if self.rodzaj_opon == "szosowe":
            predkosc -= 3
        elif self.rodzaj_opon == "gorskie":
            predkosc += 1
        elif self.rodzaj_opon == "miejskie":
            predkosc += 2

        if self.rozmiar == "niemowlęce":
            predkosc += 4
        elif self.rozmiar == "młodziezowe":
            predkosc += 3
        elif self.rozmiar == "dorosle":
            predkosc += 2

        if self.material == "carbon":
            predkosc += 10
        elif self.material == "stal":
            predkosc += 5
        elif self.material == "aluminium":
            predkosc += 7

        if self.amortyzacja == "bdb":
            predkosc += 5
        elif self.amortyzacja == "db":
            predkosc += 3
        elif self.amortyzacja == "dst":
            predkosc += 2

        if self.przerzutki == "12":
            predkosc += 4
        elif self.przerzutki == "9":
            predkosc += 3
        elif self.przerzutki == "7":
            predkosc += 2

        if self.hamulce == "tarczowe":
            predkosc += 8
        elif self.hamulce == "hydrauliczne":
            predkosc += 6
        elif self.hamulce == "rolkowe":
            predkosc += 4

        return predkosc


rower1 = Rower("cross", "szosowy", "szosowe", "dorosle", "stal", "bdb", "9", "rolkowe")
print(rower1.obliczanie_ceny())
print(rower1.v_max()) 

