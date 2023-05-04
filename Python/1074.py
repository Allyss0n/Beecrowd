n_casos = int(input())
n_in = 0
n_out = 0
for i in range(n_casos):
    x = int(input())
    if x%2==0 and x>0:    
        print("EVEN POSITIVE")
    elif x%2==0 and x<0:
        print("EVEN NEGATIVE")
    elif x%2!=0 and x>0:
        print("ODD POSITIVE")
    elif x%2!=0 and x<0:
        print("ODD NEGATIVE")
    else:
        print("NULL")     