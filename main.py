import matplotlib.pyplot as plt

print("Sveiks soļu skaitītājā!")
print("Ievadi, cik soļus nogāji katru dienu šonedēļ.\n")

dienas = ["Pirmdiena", "Otrdiena", "Trešdiena", "Ceturtdiena", "Piektdiena", "Sestdiena", "Svētdiena"]
soli_nedela = []

# raksti
for diena in dienas:
    while True:
        try:
            ievade = int(input(f"{diena}: "))
            if ievade < 0:
                print("Lūdzu, ievadi pozitīvu skaitli.")
            else:
                soli_nedela.append(ievade)
                break
        except ValueError:
            print("Lūdzu, ievadi veselus skaitļus!")

# vid
kopejie_soli = sum(soli_nedela)
videjais = kopejie_soli / len(soli_nedela)

# parad
print("\n----------------------")
print("Nedēļas rezultāti:")
for i in range(len(dienas)):
    print(f"{dienas[i]}: {soli_nedela[i]} soļi")
print("----------------------")
print(f"Kopā nedēļā noiets: {kopejie_soli} soļi")
print(f"Vidēji dienā: {round(videjais, 2)} soļi")
print("Lielisks darbs – turpini kustēties!")

# saglaba
with open("nedēļas_soļi_rezultāti.txt", "w", encoding="utf-8") as fails:
    fails.write("Soļu skaitītāja nedēļas rezultāti:\n")
    for i in range(len(dienas)):
        fails.write(f"{dienas[i]}: {soli_nedela[i]} soļi\n")
    fails.write(f"\nKopā: {kopejie_soli} soļi\n")
    fails.write(f"Vidēji dienā: {round(videjais, 2)} soļi\n")

print("\nRezultāti saglabāti failā 'nedēļas_soļi_rezultāti.txt'.")

# vnk grafiks
plt.figure(figsize=(10, 5))
plt.bar(dienas, soli_nedela, color='skyblue')
plt.title('Soļu skaits pa dienām')
plt.xlabel('Diena')
plt.ylabel('Soļu skaits')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()