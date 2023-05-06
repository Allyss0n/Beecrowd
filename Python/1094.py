n_casos = int(input())
N_C = 0
N_R = 0
N_S = 0
nt = 0
for i in range(n_casos):
    n1,n2 = input().split()
    n1 = int(n1)
    n2 = str(n2)
    nt +=n1
    if n2 == 'C':
        N_C += n1
    elif n2 == 'R':
        N_R += n1
    elif n2 == 'S':
        N_S += n1
    
print("Total: {} cobaias".format(nt))
print("Total de coelhos: {}".format(N_C))
print("Total de ratos: {}".format(N_R))
print("Total de sapos: {}".format(N_S))
print("Percentual de coelhos: {:.2f} %".format(N_C*100/nt))
print("Percentual de ratos: {:.2f} %".format(N_R*100/nt))
print("Percentual de sapos: {:.2f} %".format(N_S*100/nt))