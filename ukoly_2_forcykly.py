#1 Pomocí cyklu for napiš program, který vypíše:

# Řádek 0
# Řádek 1
# Řádek 2
# Řádek 3
# Řádek 4

for radek in range(5):
  print ("Řádek", radek, sep=" ")

#2 Vypiš lichá čísla od jedné do jedenácti pomocí příkazu for a funkce range.

for i in range (1, 13, 2):
  print(i, end=" ")


#3 Pomocí cyklu for napiš program, který vypíše:

# 1 na druhou je 1
# 2 na druhou je 4
# 3 na druhou je 9
# 4 na druhou je 16


from math import pow
for i in range (1, 5):
  print (i, "na druhou je", pow(i, 2), ".")


#4 Pomocí cyklů for a parametru end pro print napiš program, který postupně z jednotlivých 'X' vypíše:

# X X X X X
# X X X X X
# X X X X X
# X X X X X
# X X X X X

for a in range (5):
  for i in range(5):
      print  ("X", end=" ")
  print()    

#5 Napiš program, který vypíše „tabulku“ s násobilkou.

# 1 2 3 4
# 2 4 6 8
# 3 6 9 12
# 4 8 12 16

for i in range(1,5):
  for j in range(1,5):
    print(i*j, end=" ")
  print()

#6 Napiš program, který postupně z jednotlivých 'X' vypíše:

# X
# X X
# X X X
# X X X X

for i in range(1,5):
  print()
  for k in range(1,i):
    print("X", end=" ")

#7 Nakresli domeček jedním tahem v turtle modu.
from turtle import forward, left, right, exitonclick
forward(50)
left(135)
forward(50*(2**0.5))
right(135)
forward(50)
left(135)
forward(25*(2**0.5))
left(90)
forward(25*(2**0.5))
left(45)
forward(50)
left(135)
forward(50*(2**0.5))
right(135)
forward(50)

exitonclick()

#8 Nakresli n-úhelník (např. čtyřúhelník, pětiúhelník), kde n zadá uživatel.
from turtle import forward, right, left, penup, pendown, exitonclick

pocet = int(input("Kolikaúhelník mám namalovat? Zadej celé číslo: "))

for i in range(pocet):
  forward(200/pocet)
  left(180 - (180 * (1 - 2/pocet)))



exitonclick()

