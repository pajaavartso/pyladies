#ukoly_01

#1 tento ukol se zabyva vypoctem povrchu a objemu krychle
strana_krychle = 2852
print("povrch krychle je", strana_krychle**2*6)
print("objem krychle je", strana_krychle**3)

#2 Změň program tak, aby délku strany mohl zadat uživatel.
strana_krychle = int(input ("Zadej hodnotu strany krychle: "))
print("povrch krychle je", strana_krychle**2*6)
print("objem krychle je", strana_krychle**3)

#3 Napiš program, který po zadání správného hesla vypíše nějakou tajnou informaci.
heslo_string = input ("Zadej tajné heslo, pokud ho víš, zříš největší tajemství této planety:")
cislo_string = input ("Pouze heslo nestačí, nyní musíš vložit číslo, které vidíš ve věštecké kouli - pokud jsi vyvolený, dozvíš se tajemství planety a vesmíru, které bylo inzerováno v předchozí hlášce:")

heslo = heslo_string == "heslo" or heslo_string == "12345" or heslo_string == "mlok"
cislo = cislo_string == "42" or cislo_string == "1"

if heslo:
  if cislo:
    print ("Černý ledňáček sedává každý pátek odpoledne na prvním oblouku Karlova mostu")
else:
  print ("Nejsi hoden informace, o kterou se ucházíš, táhni, lotře!")

#4 Napiš program, který píše hlášky podle zadané rychlosti chůze, váhy ulovené ryby, počtu tykadel, teploty vody nebo třeba vzdálenosti od rovníku.

vaha = float(input("Kolik kg vážil tvůj poslední ulovený losos?: "))
if vaha >= 5:
  print ("Hurááá, máš lososa jak Brno!")
elif vaha <= 0:
  print ("S nulovou a zápornou váhou na nás nechoďte!")
else vaha:
  print ("Nelov pořád takový mrňata!")

print ("Díky, že jsme mohli posoudit váš úlovek!")

#5 Zkus napsat hru Kámen, nůžky, papír. Jak na to:Vytvoř si dvě proměnné, tah_cloveka a tah_pocitace. Nastav tah_pocitace na "kámen", na tah_cloveka se uživatele zeptej. Vypiš výsledky hry dle tahu člověka - buď 'Plichta.', 'Počítač vyhrál.' nebo 'Vyhrála jsi!

#hra Kamen, nuzky, papir
user_action = input ("Co volíte, kámen, nůžky, nebo papír?: ")
computer_action = ("kámen")

if user_action == computer_action:
    print(f"Oba jste zvolili" {user_action} ",je to tedy plichta!")
elif user_action == "kámen":
    if computer_action == "nůžky":
        print("Kámen rozbíjí nůžky na padrť! Vyhráváte!")
    else:
        print("Papír zabalí a zneškodní kámen, vaše prohra!")
elif user_action == "papír":
    if computer_action == "kámen":
        print("Papír zabalí a zneškodní kámen! Vyhráváte!")
    else:
        print("Nůžky rozstříhají papír na padrť! Vaše prohra!")
elif user_action == "nůžky":
    if computer_action == "papír":
        print("Nůžky rozstříhají papír na padrť! Vyhráváte!")
    else:
        print("Kámen rozbíjí nůžky na padrť! Vaše prohra.")
print ("Díky za zahrání naší duchaplné hry!")

#6 Zkus přepsat hru Kámen, nůžky, papír z předchozího úkolu pomocí and a or. Dokážeš docílit toho, aby se každý z řetězců 'Plichta.', 'Počítač vyhrál.' a 'Vyhrála jsi!' objevil v programu jen jednou, aniž bys tyhle řetězce musela přiřazovat do proměnných?

user_action = input ("Co volíte, kámen, nůžky, nebo papír?: ")
computer_action = ("kámen")

if user_action == computer_action:
    print(f"Oba jste zvolili" {user_action}. ", je to tedy plichta!")
elif user_action == "kámen" and computer_action == "nůžky" or user_action == "papír" and computer_action == "kámen" or user_action == "nůžky" and computer_action = "papír" :
        print("Výhra!")
elif user_action == "papír" and computer_action == "nůžky" or user_action == "kámen" and computer_action == "papír" or user_action == "nůžky" and computer_action == "kámen":
        print("Prohra!")
print ("Díky za zahrání naší duchaplné hry!")