"""
Verifique se um eleitor está apto a votar:
idade= 0 a 15/ 16 a 70/ >71 /e calcualar quantos anos faltam para ele poder votar ou deixar de votar.
"""
x = int(input("Digite um numero:"))
if x  > 0 and x < 17:
    print("Não obrigatório, menor que 16 anos")
elif x>=18 and x <=70:
    print("Pode votar")
else:
    print("Opcional")




