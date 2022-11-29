#1 Vytvoř funkci, která dostane jako argument příjmení a zkusí podle něj uhodnout pohlaví. Funkce bude vracet řetězec "žena" nebo "muž". Funkce bude součástí programu, který se na příjmení zeptá a následně vypíše odhad pohlaví uživatele.

surname=input("Jaké je Vaše příjmení?")
def odhad_pohlavi(surname):
  if surname.endswith("ová") or surname.endswith("ova"):
    return("Vaše příjmení je pravděpodobně ženské.")
  elif surname.endswith("ská") or surname.endswith("ska"):
    return("Vaše příjmení je pravděpodobně ženské.")
  elif surname.endswith("á"):
    return ("Vaše příjmení je pravděpodobně ženské.")
  else:
    return("Vaše příjmení je pravděpodobně mužské.")

print(odhad_pohlavi(surname))


#2 Napiš funkci, která dostane jako argument identifikační číslo (např. rodné číslo, číslo platební karty, číslo OP) a která vrátí řetězec, kde jsou všechna čísla mimo posledních čtyř nahrazena symbolem X.

#např. pro 1234567 funkce vrátí XXX4567

retezec = input("Prosím, zadej jakékoli své identifikační číslo: ")
def id(retezec):
  return ('X'*(len(retezec) - 4)+retezec[-4:])

print(id(retezec))


#3 Změň funkci ano_nebo_ne z materiálů k lekci Vlastní funkce (sekce Vracení) tak, aby se místo ano se dalo použít i a, místo ne i n a aby se nebral ohled na velikost písmen a mezery před/za odpovědí.

#Textům jako možná nebo no tak určitě by počítač dál neměl rozumět.

def ano_nebo_ne(otazka):
#Vrátí True nebo False, podle odpovědi uživatele

    while True:
        odpoved=input(otazka)
        if odpoved.lower().strip() == 'ano' or odpoved.lower().strip()=="a":
            return True
        elif odpoved.lower().strip() == 'ne' or odpoved.lower().strip() == 'n':
            return False
        else:
            print('Nerozumím! Odpověz "ano" nebo "ne" nebo "a" či "n".')

if ano_nebo_ne('Chceš si zahrát hru? '):
    print('OK! Ale napřed si ji musíš naprogramovat.')
else:
    print('Škoda.')


#4 Napiš funkci, která dostane jako parametr číslo a zjistí, jestli je sudé. Funkce by měla vracet True nebo False.

def sude (x):
  if x % 2 == 0:
    return True
  else:
    return False

print(sude(30))


#5 Napiš funkci, která dostane jako parametry tři čísla a zjistí, jestli je jejich součet větší než 10. Funkce by měla vracet vracet True nebo False.

def soucet_10 (x, y, z):
  if (x+y+z) > 10:
    return True
  else:
    return False

print(soucet_10(2, 5, 18))


#6 Napiš funkci, která vypíše čísla od jedné do 100, ale:

# Pokud je číslo dělitelné třemi, napíše místo něj "bum".
# Pokud je číslo dělitelné pěti, napíše místo něj "bác".
# Pokud je číslo dělitelné pěti i třemi zároveň, napíše místo toho "bum-bác".

def delitelnost():
  for i in range (1,101):
    if i%3 == 0 and i%5==0:
      print ("Bumbác.")
    elif i%5 == 0:
      print("Bác.")
    elif i%3 ==0:
      print("Bum.")
    else:
      print(i)

#7 Napiš funkci vyhodnot, která dostane řetězec s herním polem 1-D piškvorek a vrátí jednoznakový řetězec podle stavu hry:

# "x" – Vyhrál hráč s křížky (pole obsahuje "xxx")
# "o" – Vyhrál hráč s kolečky (pole obsahuje "ooo")
# "!" – Remíza (pole neobsahuje "-", a nikdo nevyhrál)
# "-" – Ani jedna ze situací výše (t.j. hra ještě neskončila)


retezec=20*"-"

def vyhodnot(x): #fce vyhodnocuje situaci v daný moment v piškvorkách
  if "xxx" in retezec:
    return ("Vyhrává hráč X!")
  elif "ooo" in retezec:
    return ("Vyhrává hráč O!")
  elif "-" not in retezec:
    return ("Toto je remíza - nikdo vedle sebe nenaskládal tři stejné symboly.")
  else:
    return ("Hra ještě neskončila!")

#8 Napiš funkci tah, která dostane řetězec s herním polem, číslo políčka (0-19), a symbol (x nebo o) a vrátí herní pole (t.j. řetězec) s daným symbolem umístěným na danou pozici.

def tah(pole, cislo_policka, symbol):
  return pole[:cislo_policka]+symbol+pole[cislo_policka+1:]


#9 Napiš funkci tah_hrace, která dostane řetězec s herním polem, zeptá se hráče, na kterou pozici chce hrát, a vrátí herní pole se zaznamenaným tahem hráče. Funkce by měla odmítnout záporná nebo příliš velká čísla a tahy na obsazená políčka. Pokud uživatel zadá špatný vstup, funkce mu vynadá a zeptá se znova.


def tah_hrace(herni_pole, symbol):
  while True:
    pozice = int(input("Na kterou pozici chceš hrát? Vyber čísla od 0 do 19: "))
    if pozice in range (0, 20):
      if "-" == herni_pole[pozice]:
         tah()
      else:
        print("Toto pole je obsazené, hraj na jiné pole! ")
        continue
    else:
      print("Musíš zadat číslo v rozsahu: ")
      continue
print (tah_hrace(20*"-", "X"))



