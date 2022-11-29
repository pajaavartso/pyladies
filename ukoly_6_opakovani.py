#1 Napiš program, který se zeptá na 3 čísla a zjistí, jestli je jejich součet větší než 10. Dokážeš jej vymyslet tak, aby funkce input byla v kódu zapsaná jen jednou? ;)

soucet = 0
for retezec in range (3):
    vstup = int(input("Zadej číslo: "))
    soucet = soucet + vstup

if soucet > 10:
  print("Součet je větší než 10.")
else:
    print("Součet je menší než 10.")


#2 Napiš program, který vypíše čísla od jedné do 100, ale:

# Pokud je číslo dělitelné třemi, napíše místo něj „bum”.
# Pokud je číslo dělitelné pěti, napíše místo něj „bác”.
# Pokud je číslo dělitelné pěti i třemi zároveň, napíše místo toho „bum-bác”.

def delitelnost(i):
  for i in range (1,101):
    if i%3 == 0 and i%5==0:
      print ("Bumbác.")
    elif i%5 == 0:
      print("Bác.")
    elif i%3 ==0:
      print("Bum.")
    else:
      print(i)

#3 Pokud máš ráda matematiku* a nebojíš se výzvy, načti od uživatele číslo n a:

# Vypočti faktoriál n! (součin všech celých čísel od 1 do n).
# Zjisti, jestli je n prvočíslo.
# Vypiš prvních n členů Fibonacciho posloupnosti (1, 1, 2, 3, 5, 8, 13, 21, …).


#faktoriál - úkol

faktorial=1
n = int(input("Zadej číslo a já ti řeknu jeho faktoriál: "))
if n<0:
    print("Faktoriál pro negativní čísla neexistuje :)")
elif n == 0:
  print("Faktoriál 0 je 1, na tom není nic zajímavého :)")
else:
  for i in range (1, n+1):
    faktorial=faktorial*i #returned value
  print("Faktoriál", n, "je", faktorial)
  
  
#prvočíslo - úkol:

n = int(input("Zadej číslo a já ti řeknu, jestli se jedná o prvočíslo: "))
if n > 1:
   for i in range(2,n):
       if (n % i) == 0:
           print(n,"není prvočíslo.")
           print(i,"krát",n//i,"je",n)
           break
   else:
       print(n,"je prvočíslo.")
      
      
#Fibonacciho posloupnost:
    
konec = int(input("Zadej mi limitní číslo pro Fibonacciho posloupnost: "))
a = 0
b = 1
while b <= konec:
  print(a," ", end="")
  print(b," ", end="")
  a = a + b
  b = b + a
if a <= konec:
  print(a)