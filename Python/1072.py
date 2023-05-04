n_casos = int(input())
n_in = 0
n_out = 0
for i in range(n_casos):
    x = int(input())
    if 9<x<21:
        n_in +=1
    else:
        n_out +=1
print(n_in ,"in")        
print(n_out,"out")