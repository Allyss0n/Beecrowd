a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
perimetro = a+b+c
area = ((a+b)*c)/2
if (a + b <= c) or (a + c <= b) or (b + c <= a):
    print("Area = {}".format(area))
else:    
    print("Perimetro = {}".format(perimetro))