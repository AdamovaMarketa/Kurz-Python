jmeno = "Marketa"
print(f"{jmeno}@czechitas.cz")

jmeno_a_prijmeni = input("Napis jmeno a prijmeni\n")
print(jmeno_a_prijmeni .upper())
print(jmeno_a_prijmeni .lower())
jmeno_a_prijmeni = jmeno_a_prijmeni .lower() .split()
print(f"{jmeno_a_prijmeni [0][0] .upper()}. {jmeno_a_prijmeni [1][0] .upper()}.")
print(f"{jmeno_a_prijmeni [0][0] .upper()}{jmeno_a_prijmeni[0][1:]} {jmeno_a_prijmeni [1][0] .upper()}{jmeno_a_prijmeni[1][1:]}")