#sum_of.list
#funkcja sumująca liste, 
#startowa lista jest pusta, is l empty? yes=0, no=pierwszy elemenet listy+reszta np. [1,2,3] = 1+[2,3]

#pseudokody
#sum of list
#1.definicujemy funkcje
#2. Funckja sprawdza, czy tabela jest pusty. Jeśli jest pusty, pokazuje warrtość 0
#3. Jeśli zbiór jest niepusty, pokazuje pierwszą wartośc z tabeli + pozostałe elementy tabeli i wykonuje tą czynnośc, do momentu aż nasza tabela będzie pusta
#4. Każde z przejśc jest sumowane od ostatniego do pierwszego i końcowo otrzymujemy wiadomość o sumie wszystkich elementów

def suma_listy(list):
    if len (list) == 0:
        return 0
    elif  len (list) > 0:
        first_element = list[0]
        list.pop(0)
        return first_element + suma_listy(list) # first_element + suma_listy(list[1:])
list1 = [1,2,4]
print (suma_listy(list1))

#n!
#1. definiujemy funkcje 
#2. fukncja oblicza silnie dla podanej liczby
#3. podajemy iż liczba n jest z przedziału od 100 do 1
#4. Program oblicza wartośc funkcjji, mnożąc podaną wartośc i mnożąc ją przez kolejne różnice wartości podanej przez kolejno wartość (n-1)*(n-2),
#  aż dojdziemy do wartości kiedy będziemy mnożyć przez 1, wtedy program się zatrzymuje i pokazuje iloczyn podanej przez nas liczby
#funckja find.max
#małe sudoku
