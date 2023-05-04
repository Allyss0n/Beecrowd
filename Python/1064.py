v1 = float(input())
v2 = float(input())
v3 = float(input())
v4 = float(input())
v5 = float(input())
v6 = float(input())
resultado=0
media = 0
v =[v1,v2,v3,v4,v5,v6]
for i in (v):
    if i>0:
        resultado += 1
        media += (i)
print ("{} valores positivos".format(resultado))
print('{:.1f}'.format(media/resultado))