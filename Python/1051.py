user_input = float(input())
if user_input>4500:
    x28 = user_input - 4500
    x28 *= 0.28
    imposto = x28 + (1500*0.18) + (1000*0.08)
    print("R$ {:.2f}".format(imposto))
elif 4501>user_input>3000.01:
    x18 = user_input - 3000
    x18 *= 0.18
    imposto = x18 + (1000*0.08)
    print("R$ {:.2f}".format(imposto))
elif 3001.00>user_input> 2000.01:
    x8 = user_input - 2000
    x8 *= 0.08
    imposto = x8 
    print("R$ {:.2f}".format(imposto))
else:
    print("Isento")
    