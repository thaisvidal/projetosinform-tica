#"F1", se N <= 10
#"F2", se N > 10 e N <= 100
#"F3", se N > 100.
numero = int(input("Digite um número: "))
if numero <= 10:
    print("F1")
elif numero <= 100:
    print("F2")
else:
    print("F3")