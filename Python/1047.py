hora_inicial, minuto_inicial, hora_final, minuto_final = input().split()
hora_inicial = int(hora_inicial)
minuto_inicial = int(minuto_inicial) 
hora_final = int(hora_final)
minuto_final = int(minuto_final)


hiconv = hora_inicial*60
hfconv = hora_final*60
total = (1440-(hiconv+minuto_inicial)) + (hfconv+minuto_final)
totalhora = int(total/60)
totalmin = (total%60)
if totalhora>=24:
    totalhora=0

if hora_final==hora_inicial and minuto_inicial==minuto_final:
        print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)".format(totalhora,totalmin))

#Mesmo dia
elif hora_final>hora_inicial:
    total = (hfconv+minuto_final) - (hiconv+minuto_inicial)
    totalhora = int(total/60)
    totalmin = (total%60)
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(totalhora,totalmin))

#Dia diferente
else:
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(totalhora,totalmin))