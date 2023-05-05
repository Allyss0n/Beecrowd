lista= []
for i in range(100):
    x = int(input())
    lista.append(x)
maior = max(lista)
a = lista.index(maior)
print(maior)
print(a+1)
