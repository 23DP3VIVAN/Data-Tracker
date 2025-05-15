dienas = ["Pirmdiena", "Otrdiena", "Trešdiena", "Ceturtdiena", "Piektdiena", "Sestdiena", "Svētdiena"]
soli_nedela = []

def ievadit_solus():
    print("\nIevadi soļu skaitu katrai nedēļas dienai:")
    dati = []
    for diena in dienas:
        while True:
            try:
                skaits = int(input(f"{diena}: "))
                if skaits >= 0:
                    dati.append((diena, skaits))
                    soli_nedela.append(skaits)
                    break
                else:
                    print("Ievadi pozitīvu skaitli!")
            except ValueError:
                print("Lūdzu, ievadi skaitli!")

    with open("step_data.txt", "w", encoding="utf-8") as f:
        for diena, skaits in zip(dienas, soli_nedela):
            f.write(f"{diena}: {skaits} soļi\n")
    print("Dati saglabāti failā 'step_data.txt'.\n")

def paradit_rezultatus():
    print("\nSoļu rezultāti pa nedēļas dienām:")
    if not soli_nedela:
        print("Nav datu par soļiem šai nedēļai.\n")
        return
    for diena, skaits in zip(dienas, soli_nedela):
        print(f"{diena}: {skaits} soļi")
    print(f"\nVidējais soļu skaits nedēļā: {sum(soli_nedela) / len(soli_nedela):.2f} soļi\n")
    print("Dati tiks saglabāti failā 'step_data.txt'.")

if __name__ == "__main__":
    ievadit_solus()
    paradit_rezultatus()