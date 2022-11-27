#Napiš funkci tah_hrace, která dostane řetězec s herním polem, zeptá se hráče, na kterou pozici chce hrát, a vrátí herní pole se zaznamenaným tahem hráče. Funkce by měla odmítnout záporná nebo příliš velká čísla a tahy na obsazená políčka. Pokud uživatel zadá špatný vstup, funkce mu vynadá a zeptá se znova.

def tah_hrace(herni_pole, symbol):

  herni_pole = 20*"-"
  while True:
    pozice = int(input("Na kterou pozici chceš hrát? Vyber čísla od 0 do 19: "))
    if pozice in range (0, 20):
      if "-" == herni_pole[pozice]:
        return herni_pole[:pozice]+symbol+ herni_pole[pozice+1:]
      else:
        print("Toto pole je obsazené, hraj na jiné pole! ")
        continue
    else:
      print("Musíš zadat číslo v rozsahu: ")
      continue
print (tah_hrace(20*"-", "X"))


# def tah(pole, cislo_policka, symbol):
# # Vrátí herní pole s daným symbolem umístěným na danou pozici
#   return pole[:cislo_policka]+symbol+pole[cislo_policka+1:]


# def tah_hrace(herni_pole):
#   cislo_policka = input("Na kterou pozici chceš hrát? Vyber čísla od 0 do 19:")
#   if cislo_policka in range (0,20):
#     return tah(herni_pole, cislo_policka, "X")

# def tah_pocitace(herni_pole):
#   #vrati tah pocitace

# def vyhodnot(herni_pole): #fce vyhodnocuje situaci v daný moment v piškvorkách
#   if "xxx" in herni_pole:
#     return ("Vyhrává hráč X!")
#   elif "ooo" in herni_pole:
#     return ("Vyhrává hráč O!")
#   elif "-" not in herni_pole:
#     return ("Toto je remíza - nikdo vedle sebe nenaskládal tři stejné symboly.")
#   else:
#     return ("Hra ještě neskončila!")

    
          


