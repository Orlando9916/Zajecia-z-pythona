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
    def __init__(self, marka, przeznaczenie):
        self.marka = marka
  #      self.rodzaj_opon = rodzaj_opon
  #      self.rozmiar = rozmiar
        self.przeznaczenie = przeznaczenie
 #       self.kolor = kolor
 #       self.waga = waga
 #       self.klasa = klasa
#        self.dodatki = dodatki
#       self.cena = 0
    def obliczanie_ceny(self):
        cena = 0
        if self.marka =="x":
            cena += 1000
        elif self.marka =="y":
            cena += 700
        elif self.marka =="z":
            cena += 500
        
        if self.przeznaczenie =="szosowy":
            cena += 100
        
        print(cena)


rower = Rower("x", "szosowy") 
rower.obliczanie_ceny()       

