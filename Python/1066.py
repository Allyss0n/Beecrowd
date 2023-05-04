v1 = float(input())
v2 = float(input())
v3 = float(input())
v4 = float(input())
v5 = float(input())
par=0
impar=0
positivo=0
negativo=0
v =[v1,v2,v3,v4,v5]
for i in (v):
    #par
    if i%2==0:
        par+=1
    elif i%2!=0:
        impar+=1
    if i>0:
        positivo+=1
    elif i<0:
        negativo+=1 
print ("{} valor(es) par(es)".format(par))
print ("{} valor(es) impar(es)".format(impar))
print ("{} valor(es) positivo(s)".format(positivo))
print ("{} valor(es) negativo(s)".format(negativo))