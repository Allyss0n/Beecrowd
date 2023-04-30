v1, v2 = input().split()
v1 = int(v1)
v2 = int(v2)
x = (24-v1) + v2
if x <25:
  print("O JOGO DUROU {} HORA(S)".format(x))
else:
  x = v2-v1
  print("O JOGO DUROU {} HORA(S)".format(x))