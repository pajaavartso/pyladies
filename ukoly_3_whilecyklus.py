#1 Napiš program, který se bude uživatele ptát na tajné heslo do té doby, než ho uživatel správně vyplní.

tajne_heslo="bubak"
uzivatel=" "
while tajne_heslo != uzivatel:
  uzivatel=input("Zadej své tajné heslo: ")
print ("Heslo je správně zadáno!")

#2 Změň program Kámen, nůžky, papír z úkolu 7 po druhé lekci tak, aby opakoval hru, dokud uživatel nezadá konec.

from random import choice

while True:
    user_action = input ("Co volíte, kámen, nůžky, nebo papír?: ")
    possible_actions = ["kámen", "nůžky", "papír"]
    computer_action = choice(possible_actions)
    print("Zvolili jste", user_action, "počítač zvolil", computer_action, end=".")
    

    if user_action == computer_action:
      print("Oba jste zvolili", user_action, "je to tedy plichta!")

    elif user_action == "kámen" and computer_action == "nůžky" or user_action == "papír" and computer_action == "kámen" or user_action == "nůžky" and computer_action == "papír" :

        print("Výhra!")

    elif user_action == "papír" and computer_action == "nůžky" or user_action == "kámen" and computer_action == "papír" or user_action == "nůžky" and computer_action == "kámen":

        print("Prohra!")

    print ("Díky za zahrání naší duchaplné hry!")

    play_again=input("Chcete hrát znovu?: a/n ")
    if play_again != "a":
      break


#3 Změň program Kámen, nůžky, papír tak, aby se tah počítače určoval náhodně.

from random import randrange

while True:
  print("Vítejte v naší hře Kámen, nůžky, papír!")
  print("Vložte číslo \n 1 pro kámen, \n 2 pro papír \n 3 pro nůžky: \n")
  user_action= int(input("Vyber 1, 2 nebo 3: "))


  if user_action == 1:
    choice_name = "kámen"
  elif user_action == 2:
    choice_name = "papír"
  else:
    choice_name = "nůžky"

  print ("Zvolili jste", user_action, "což je", choice_name, end=".")
  print("Teď si vybere počítač!")
  computer_action = randrange(1, 4)

  if computer_action == 1:
    comp_choice_name = "kámen"
  elif computer_action == 2:
    comp_choice_name = "papír"
  else:
    comp_choice_name = "nůžky"

  print ("Počítač zvolil", computer_action, "což je", comp_choice_name, end=".")

  if user_action == computer_action:
    print("Oba jste zvolili", user_action, "je to tedy plichta!")

  elif user_action == 1 and computer_action == 3 or user_action == 2 and computer_action == 1 or user_action == 3 and computer_action == 2 :
    print("Výhra!")

  elif user_action == 2 and computer_action == 3 or user_action == 1 and computer_action == 2 or user_action == 3 and computer_action == 1:

    print("Prohra!")

  print ("Díky za zahrání naší duchaplné hry!")

  play_again=input("Chcete hrát znovu?: a/n ")
  if play_again != "a":
    break


#4 Napiš program, který se ptá uživatele na čísla do té doby, než zadá 0. Poté vypíše nejmenší ze zadaných čísel. (Pozor: nula se mezi porovnávaná čísla nepočítá.)

uzivatel = 0
nejmensi = 101  


while True:
    uzivatel = int(input("Prosim zadej hodnotu od 0 do Kladna: "))
    if uzivatel == 0:
        break
    
    if uzivatel < 0:
        print("Říkám do Kladna, ne do Záporna :) :(\n")
        continue
   
    

    if uzivatel < nejmensi:
        nejmensi = uzivatel

if uzivatel == 0:
    print("Nejmensi cislo je:", (nejmensi))
    print("\nDiky!")


#5 Napiš program, který simuluje tuto hru:První hráč hází kostkou (t.j. vybírají se náhodná čísla od 1 do 6), dokud nepadne šestka. Potom hází další hráč, dokud nepadne šestka i jemu. Potom hází hráč třetí a nakonec čtvrtý. Vyhrává ten, kdo na hození šestky potřeboval nejvíc hodů. (V případě shody vyhraje ten, kdo házel dřív.) Program by měl vypisovat všechny hody a nakonec napsat, kdo vyhrál.

from random import randrange
nejvetsi=0
kdo_mel_nejvetsi=0
for hrac in range(4):
  print("Hráč číslo ",hrac)
  pocet_hodu=0
  while True:
    hod=randrange(1,7)
    pocet_hodu=pocet_hodu+1
    if hod==6:
      print("Nyní jsi hodil",hod, ".")
      break
    if hod<6:
      print("Nyní jsi hodil", hod,"potřebuješ hodit šestku!" )

  if pocet_hodu > nejvetsi:
    nejvetsi=pocet_hodu
    kdo_mel_nejvetsi=hrac

  print("Podařilo se ti hodit šestku na ", pocet_hodu, "pokus.")

print("Vyhrál uzivatel, co hodil šestku na ", nejvetsi, "pokus.")

print ("Vyhrál hráč", kdo_mel_nejvetsi)


#6 Napiš program, který postupně načte od uživatele dvě čísla a jednoznakový řetězec – buď '+', '-', '*' nebo '/'. Program provede na číslech příslušnou operaci.

prvni_cislo = int(input("Prosím, zadej první libovolné číslo: "))
druhe_cislo = int(input("Prosím, zadej druhé libovolné číslo: "))
oper = input("Prosím, zadej matematický operátor +, -, *, nebo /: ")
if oper == "+":
  print(prvni_cislo+druhe_cislo)
elif oper == "-":
  print (prvni_cislo-druhe_cislo)
elif oper == "*":
  print (prvni_cislo*druhe_cislo)
elif oper == "/":
  print(prvni_cislo/druhe_cislo)
else:
  print("Zadej něco pořádného, třeba +, -, * nebo / : ")


#7 Pomocí cyklu for a příkazu if napiš program, který vypíše následující řádky. Funkci print volej pouze uvnitř v cyklu:

# první řádek
# není první
# není první
# není první


for radek in range(4):
  if radek == 0:
    print("první řádek")
  else:
    print("není první")



