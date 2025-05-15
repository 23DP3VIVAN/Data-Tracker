from ascii import print_ascii_art
from login import login
from menu import show_menu
from step_data import ievadit_solus, paradit_rezultatus

def galvena_programma():
    print_ascii_art()
    if not login():
        return

    while True:
        choice = show_menu()
        if choice == "1":
            ievadit_solus()
        elif choice == "2":
            paradit_rezultatus()
        elif choice == "3":
            print("Uz redzēšanos!")
            break
        else:
            print("Nederīga izvēle, mēģini vēlreiz.\n")

if __name__ == "__main__":
    galvena_programma()