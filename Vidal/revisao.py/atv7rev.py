# solicita o nome do aluno
nome = input("Digite o nome do aluno: ")

# solicita as duas notas (convertendo para float, já que podem ter casas decimais)
nota1 = float(input("Digite a primeira nota (0 a 10): "))
nota2 = float(input("Digite a segunda nota (0 a 10): "))

# calcula a média
media = (nota1 + nota2) / 2

# exibe os resultados
print("\n--- Resultado ---")
print("Aluno:", nome)
print("Nota 1:", nota1)
print("Nota 2:", nota2)
print("Média:", media)