dienas = ["Pirmdiena", "Otrdiena", "Trešdiena", "Ceturtdiena", "Piektdiena", "Sestdiena", "Svētdiena"]
soli_nedela = []

def ievadit_solus():
    print("\nIevadi soļu skaitu katrai nedēļas dienai:")
    for diena in dienas:
        while True:
            try:
                skaits = int(input(f"{diena}: "))
                if skaits >= 0:
                    soli_nedela.append(skaits)
                    break
                else:
                    print("Ievadi pozitīvu skaitli!")
            except ValueError:
                print("Lūdzu, ievadi skaitli!")
    print("Dati saglabāti!\n")

def paradit_rezultatus():
    if not soli_nedela:
        print("Nav datu, lūdzu vispirms ievadi soļus.")
        return

    kopa = sum(soli_nedela)
    videjais = round(kopa / len(soli_nedela), 2)

    print("\nTavi rezultāti:")
    for i in range(len(dienas)):
        print(f"{dienas[i]}: {soli_nedela[i]} soļi")
    print(f"\nKopā: {kopa} soļi")
    print(f"Vidēji dienā: {videjais} soļi\n")
