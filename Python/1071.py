x = int(input())
y = int(input())
impares = []

if x<y:
    for i in range(x+1,y):       
        if i%2 !=0:
            impares.append(i)
    

elif y<x:
    for i in range(y+1,x):
        if i%2 !=0:
            impares.append(i)
    if x<0:
        impares.append(x)        
              
print(sum(impares))