#1 Napiš funkci, která dostane jako argumenty seznam zvířat a slovo a zjistí, jestli je toto slovo v seznamu. „Zjistí“ znamená, že funkce vrátí True nebo False.

zvirata = ["pes", "kočka", "králík", "had"]
slovo = input("Dej mi slovo, a já ti vrátím hodnotu True/false podle toho, jestli v seznamu je: ")
def je_slovo_v_seznamu (zvirata, slovo):
  if slovo in zvirata:
    return True
  else:
    return False

print(je_slovo_v_seznamu(zvirata, slovo))


#2 Napiš funkci, která dostane jako argument seznam domácích zvířat a vrátí seznam těch, která jsou kratší než 5 písmen.

zvirata = ["pes", "kočka", "králík", "had"]

def zvire_ma_min_nez(zvirata):
  vysledny_seznam=[]
  for zvire in zvirata:
    if len(zvire) < 5:
      vysledny_seznam.append(zvire)
    return vysledny_seznam


#3 Napiš funkci, která dostane jako argument seznam domácích zvířat a vrátí seznam těch, která začínají na k.

zvirata = ["pes", "kočka", "králík", "had"]

def zacina_na_k(zvirata):
  vysledny_seznam = []
  for zvire in zvirata:
    if zvire.startswith("k"):
      vysledny_seznam.append(zvire)
  return vysledny_seznam


#4 Napiš program, který seřadí seznam domácích zvířat podle abecedy.

zvirata = ["pes", "kočka", "králík", "had"]
srovnana_zvirata = sorted(zvirata)
print(srovnana_zvirata)

# 5 Napiš funkci, která dostane dva seznamy jmen zvířat a vrátí zvířata, která jsou v obou seznamech současně (průnik množin: první ∩ druhá)

def prunik_zvirat(zvirata):
	prunik = []
	for zvire in zvirata:
  		if zvire in zvirata_2:
        return prunik.append(zvire)
