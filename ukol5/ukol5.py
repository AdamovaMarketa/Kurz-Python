teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]
""" ráno, v poledne, večer, v noci
Vytvoř seznam průměrných teplot pro každý den.
Vytvoř seznam ranních teplot.
Vytvoř seznam nočních teplot.
Vytvoř seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu."""

def prumer(seznam):
    return sum(seznam) / len(seznam)

prumerne_teploty = [prumer(den) for den in teploty]
print(prumerne_teploty)

ranni_teploty = [den[0] for den in teploty]
print(ranni_teploty)

nocni_teploty = [den[3] for den in teploty]
print(nocni_teploty)

poledne_noc = [[den[1], den[3]] for den in teploty]
print(poledne_noc)