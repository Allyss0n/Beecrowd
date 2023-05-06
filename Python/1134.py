alcool= 0
gasolina =0 
diesel =0
x = int(input())
while x!=0:
    x = int(input())
    if x>4:
        pass
    else:
        if x==1:
            alcool+=1
        elif x==2:
            gasolina+=1
        elif x==3:
            diesel+=1
        elif x==4:
            print("MUITO OBRIGADO")
            print("Alcool:",alcool)
            print("Gasolina:",gasolina)
            print("Diesel:",diesel)
            break