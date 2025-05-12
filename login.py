users = {}

def register():
    print("Reģistrācija")
    username = input("Izvēlieties lietotājvārdu: ")
    if username in users:
        print("Šis lietotājvārds jau eksistē.\n")
        return False
    password = input("Izvēlieties paroli: ")
    users[username] = password
    print("Reģistrācija veiksmīga!\n")
    return True

def login():
    while True:
        print("1. Ielogoties")
        print("2. Reģistrēties")
        choice = input("Izvēlies darbību (1/2): ")

        if choice == "2":
            register()
        elif choice == "1":
            username = input("Lietotājvārds: ")
            password = input("Parole: ")
            if username in users and users[username] == password:
                print(f"Sveicināts, {username}!\n")
                return True
            else:
                print("Nepareizs lietotājvārds vai parole. Mēģini vēlreiz.\n")
        else:
            print("Nederīga izvēle, mēģini vēlreiz.\n")