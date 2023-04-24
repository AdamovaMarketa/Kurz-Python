"""
ukol-04
Zadání
Uvažuj, že píšeš jednoduchou aplikaci pro zasílání SMS zpráv. Napiš program, který provede následující činnosti:

Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát.
Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát.
Tvůj program bude obsahovat dvě funkce:

První funkce ověří telefonní číslo. Uvažuj, že telefonní číslo může být devítimístné nebo třináctimístné (pokud je na začátku předvolba "+420"). Funkce ověří, jestli je číslo platné. Pokud je platné, vrátí hodnotu True, jinak vrátí hodnotu False.
Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.
Tvůj program nejprve ověří pomocí první funkce správnost telefonního čísla. Pokud není platné, vypíše chybu, v opačném případě se zeptá na text zprávy a pomocí druhé funkce určí její cenu, kterou vypíše uživateli.

Tipy:

Nemusíte kontrolovat, zda uživatel zadal skutečně číslo, či zda jsou tam i jiné znaky. To jsme v kurzu zatím neřešili.
Pro kontrolu předvolby použijte slicing (viz první lekce) pro získání prvních 4 znaků řetězce. Ty porovnejte s řetězcem "+420".
"""

def overit_tel(telefon):
    if len(telefon) == 9:
        return True
    elif len(telefon) == 13 and telefon[0:4] == "+420":
        return True
    else:
        return False

def cena_zpravy(text):
    delka = len(text)
    cela_cast = delka // 180 
    zbytek = delka % 180
    cena = cela_cast * 3
    if zbytek >= 1:
        cena = cena + 3
    return cena

cislo = input("Zadej číslo, kam chceš zaslat zprávu sms.\n")
if overit_tel(cislo):
    zprava = input("Zadej text sms zprávy.\n")
    vysledek = cena_zpravy(zprava)
    print(f"Cena sms zprávy je {vysledek} Kč - počet znaků: {len(zprava)}.")
else:
    print("Chybný formát tel. čísla.")
    exit()



 