f1,f2 = input().split()
f1 = float(f1)
f2 = float(f2)

f1 = (f1/100) + 1
f2 = (f2/100) + 1
r = ((100 * f1 * f2)-100)
print("{:.6f}".format(r))            
                                   