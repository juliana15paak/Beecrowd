vertebral = input()
classe = input()
alimentar = input()
if vertebral == "vertebrado":
    if classe == "ave":
        if alimentar == "carnivoro":
            print("aguia")
        elif alimentar == "onivoro":
            print("pomba")
    elif classe == "mamifero":
        if alimentar == "onivoro":
            print("homem")
        elif alimentar == "herbivoro":
            print("vaca")
elif vertebral == "invertebrado":
    if classe == "inseto":
        if alimentar == "hematofago":
            print("pulga")
        elif alimentar == "herbivoro":
            print("lagarta")
    elif classe == "anelideo":
        if alimentar == "hematofago":
            print("sanguessuga")
        elif alimentar == "onivoro":
            print("minhoca")
