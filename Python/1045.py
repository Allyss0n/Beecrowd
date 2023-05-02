medidas = input().split()
medidas = [float(i) for i in medidas]

medidas.sort(reverse=True)


a = float(medidas[0])
b = float(medidas[1])
c = float(medidas[2])


if a>=(b+c):
    print("NAO FORMA TRIANGULO")
else:
    if (a**2)==(b**2)+(c**2):
        print("TRIANGULO RETANGULO")
    elif (a**2)>(b**2)+(c**2):
        print("TRIANGULO OBTUSANGULO")    
    elif (a**2)<(b**2)+(c**2):
        print("TRIANGULO ACUTANGULO")    
    if a==b==c:
        print("TRIANGULO EQUILATERO")
    elif a==b or b==c:
        print("TRIANGULO ISOSCELES")