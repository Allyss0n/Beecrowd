n_casos = int(input())
for i in range(n_casos):
    n1,n2 = input().split()
    n1 = int(n1)
    n2 = int(n2)
    mdc = n1
    resto=n1%n2;
    while(resto!=0):
        n1    = n2;
        n2    = resto;
        resto = n1%n2;         
    print(n2)
    #while n1 % mdc != 0 or n2 % mdc != 0: 
    #    mdc = mdc - 1
    #print(mdc)