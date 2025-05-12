def login():
    print("Lūdzu, ielogojies")
    username = input("Lietotājvārds: ")
    password = input("Parole: ")

    if username == "lietotajs" and password == "parole123":
        print(f"Sveicināts, {username}!\n")
        return True
    else:
        print("Nepareizs lietotājvārds vai parole.\n")
        return False
