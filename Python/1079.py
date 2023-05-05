n_casos = int(input())

for i in range(n_casos):
    n1,n2,n3 = input().split()
    n1 = float(n1)
    n2 = float(n2)
    n3 = float(n3)    

    r = ((n1*2) + (n2*3) + (n3*5))/10
    print("{:.1f}".format(round(r,1)))