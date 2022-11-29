#1 Vytvoř funkci pocet_vterin, která bude mít dva argumenty: čas v minutách a čas ve vteřinách. A bude vracet celkový počet vteřin.

def pocet_vterin(min, sec): # program na zadání mínut či sekund a přepočítání na sekundy
  return (min*60) + sec
print(pocet_vterin(2,30)) #například


#2 Napiš funkci, která vrátí maximální hodnotu ze tří zadaných čísel. Zjištění maxima naprogramuj sama, pomocí příkazů if.

def maximum(a, b, c):
#maximální hodnota ze 3 čísel
  if a>=b and a>=c:
    return a
  elif b>=c and b>=a:
    return b
  else:
    return c

#3 Vytvoř funkci, která spočítá Body Mass Index pro kočky. Vstupem (parametry) funkce bude obvod hrudníku (cm) a délka zadní nohy od kolena ke kotníku (cm). Funkce vrátí číslo feline body mass index (fBMI).

#Postup výpočtu fBMI: 1. Vydělit obvod hrudníku 0.7062 a odečíst délku nohy. 2. Vydělit výsledek 0.9156. 3. Od výsledku bodu 2 odečíst délku nohy.

def fbmi(hrudnik_cm, noha_cm):
  return ((hrudnik_cm/0.7062 - noha_cm)/0.9156)-noha_cm
print(fbmi(60, 30)) #například


#4 Vytvoř funkci nakresli_n_uhelnik, která vykreslí pro zadaný počet stran n-úhelník. Pomocí této funkce vykresli následující obrázek:
#n-úhelníky

from turtle import forward, right, left, penup, pendown, exitonclick
pocet = int(input("Kolikaúhelník mám namalovat? Zadej celé číslo: "))
def n_uhelnik(pocet):
  for j in range(4):
    for i in range(pocet):
        forward(200/pocet)
        left(180 - (180 * (1 - 2/pocet)))
    penup()
    forward(100)
    pendown()
    pocet=pocet + 1
print(n_uhelnik(pocet))

exitonclick()


#5 Napiš funkci, která s pomocí cyklu for a příkazu if vypíše z jednotlivých 'X' a mezer následující obrazec:

# X X X X X X
# X         X
# X         X
# X         X
# X         X
# X X X X X X

def xka(x):
  for radek in range(0,x):
    for sloupec in range(0,x):
      if radek == 0 or radek == x-1 or sloupec == 0 or sloupec == x-1:
        print("X ", end="")
      else:
        print("  ", end="") 
    print("")
print(xka(6))


#6 Napiš funkci, která bude mít jako parametr jedno číslo a vrátí "Bum", je-li toto číslo liché, a "Bác", je-li toto číslo sudé.

def even_odd(x):
  if x % 2 == 0:
      return("Bác.")
  else:
     return("Bum.")
print(even_odd(3))


#7 Napiš funkci, která bude mít jako parametr jedno číslo (n) a vypíše n řádek. Na prvním řádku bude "Bum", na druhém "Bác", na třetím "Bum", atd. Využij funkci z předchozího úkolu.

def bum_bac(x):
  for i in range (x):
    even_odd()

