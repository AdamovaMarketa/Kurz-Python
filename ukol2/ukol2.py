sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

kod = input("Jaký je kód součástky?\n")

if not(kod in sklad):
    print("Součástka není skladem.\n")
    exit()

pocet = int(input("Jaké množství součástky?\n"))

if pocet > sklad[kod]:
    print(f"Lze prodat pouze {sklad[kod]} kusů.")
    sklad.pop(kod)

else:
    print("Poptávku lze splnit.")
    sklad[kod] = sklad[kod] - pocet

# Vypsat aktuální seznam
print(sklad)
