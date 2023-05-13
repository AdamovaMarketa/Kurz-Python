"""
Vytvoř program pro evidenci aut malé autopůjčovny. Půjčovna má 2 automobily:

Registrační značka	Značka a typ vozidla	Počet najetých kilometrů
4A2 3020	Peugeot 403 Cabrio	47534
1P3 4747	Škoda Octavia	41253
Vytvoř třídu Auto, která bude obsahovat informace o autech, které půjčovna nabízí. Třída bude mít tyto atributy:

registrační značka automobilu registracni_znacka,
značka a typ vozidla typ_vozidla,
počet najetých kilometrů najete_km,
informaci o tom, jestli je vozidlo aktuálně volné dostupne (pravdivostní hodnota -- True pokud je volné a False pokud je vypůjčené).
Vytvoř metodu __init__() pro třídu Auto. Registrační značku, značku a typ vozidla a počet kilometrů získej jako parametry funkce __init__ a ulož je jako atributy objektu. Poslední atribut rovnou nastav jako True, tj. na začátku je vozidlo vždy volné.

Vytvoř objekty, které reprezentují oba automobily půjčovny.

Třídě Auto přidej metodu pujc_auto(), která nebude mít (kromě obligátního self) žádný parametr. 
Funkce zkontroluje, jestli je vozidlo aktuálně volné. Pokud je volné, změní hodnotu atributu dostupne, 
který určuje, zda je vozidlo půjčené, a vrátí text "Potvrzuji zapůjčení vozidla". Pokud je vozidlo již půjčené, 
vrátí text "Vozidlo není k dispozici".

Dále tříde Auto přidej funkci get_info(), která vrátí informaci o vozidle (stačí registrační značka a značka a typ vozidla) jako řetězec.

Nakonec do programu (mimo třídu) napiš dotaz na uživatele, jakou značku si uživatel přeje půjčit. 
Uživatel může zadávat hodnoty Peugeot nebo Škoda. Jakmile si uživatel vybere značku, 
vypiš informaci o vozidle pomocí funkce get_info() a následně použij funkci pujc_auto().

Otestuj, že program nedovolí půjčit stejné auto dvakrát.


---
BONUS
---
Přidej třídě Auto metodu vrat_auto(), která bude mít (krom obligátního self) 2 parametry, 
a to je stav tachometru při vrácení a počet dní, po které zákazník auto používal. 
Ulož stav tachometru do atributu objektu. Nastav vozidlo jako volné.

Dále ve funkci vypočti cenu za půjčení. Cena je 400 Kč na den, pokud měl zákazník celkem auto méně než týden, 
a 300 Kč na den, pokud měl zákazník auto déle. Cena je stejná pro obě auta. 
Vlož cenu do nějakého informativního textu a ten vrať pomocí klíčového slova return.
"""

class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupnost = True

    def pujc_auto(self):
        if self.dostupnost:
            self.dostupnost = False
            print("Potvrzuji zapůjčení vozidla")
        else:
            print("Vozidlo není k dispozici")

    def get_info(self):
        return (f"{self.registracni_znacka}, {self.typ_vozidla}")
    
    def vrat_auto(self, tachometr, dny):
        if self.dostupnost:
            return(f"Auto nebylo zapujčeno.")

        self.najete_km = tachometr
        self.dostupnost = True
        if dny < 7:
            cena = 400*dny
        else:
            cena = 300*dny
        return(f"Výsledná cena za {dny} dní je {cena} Kč.")        

        
auto_1 = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
auto_2 = Auto("1P3 4747", "Škoda Octavia", 41253)

vypujcka = input("Jakou značku si přeješ pujčit?\nVyber: Peugeot / Škoda\n")
if vypujcka == "Peugeot":
    print(auto_1.get_info())
    auto_1.pujc_auto()
elif vypujcka == "Škoda":
    print(auto_2.get_info())
    auto_2.pujc_auto()
else:
    print("Nezadal jsi platnou hodnotu: Peugeot / Škoda")

print("\nTEST")  
auto_1.pujc_auto()
auto_2.pujc_auto()
        
print(auto_1.vrat_auto(48000, 30))
print(auto_1.vrat_auto(48000, 30))
print(auto_2.vrat_auto(41500, 3))

auto_1.pujc_auto()
auto_2.pujc_auto()




