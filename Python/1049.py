t1 = str(input())
t2 = str(input())
t3 = str(input())

if t1=="vertebrado":
    if t2=="ave":
        if t3=="carnivoro":
            print("aguia")
        elif t3=="onivoro":
            print("pomba")
    elif t2=="mamifero":
        if t3=="onivoro":
            print("homem")
        elif t3=="herbivoro":
            print("vaca")
if t1=="invertebrado":
    if t2=="inseto":
        if t3=="hematofago":
            print("pulga")
        elif t3=="herbivoro":
            print("lagarta")
            
    elif t2=="anelideo":
        if t3=="hematofago":
            print("sanguessuga")
        elif t3=="onivoro":
            print("minhoca")