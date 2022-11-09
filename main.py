print("""************************************

Faktorielle finden Programm

Um Programm zu beenden 'x' drücken.
************************************
""")

while True:
    zahl = input("Zahl:")
    if (zahl == "x"):
        print("Programm wird beendet.")
        break
    else:
        zahl = int(zahl)

        faktorielle = 1

        for i in range (2,zahl+1):
            
            faktorielle *= i
        print("Faktorielle",faktorielle)
