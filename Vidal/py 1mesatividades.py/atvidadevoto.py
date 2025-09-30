#Verifique se um dado numero digitado pelo usuario é maor de idade e calcule quantos anos faltam pra ele votar ou deixar de votar.
while True: # Código de ativação do loop
    AMARELO = "\033[33m" # Cor amarela
    idade = int(input("Digite sua idade para votar ou digite 0 para sair 👀:")) # O usuário digita um número inteiro pois int significa inteiro
    if idade == 0: #quando o usuário digitar 0 o programa encerra o loop
        break # Saindo do programa/looping pois break é para sair dele 
    if idade >= 16 and idde < 18: #se tiver entre 16 e 17 anos
        print("And não é obrigatório votar, é sua decisão querer ou não 😛!")
        #printando na tela isso
    elif idade >= 18 and idade <= 70: #Se for maior ou igual a 18 e menor ou igual a 70
        print("Você é maior de idade. O voto é obrigatório ou precisa ser justificado 👨!")
        #printando na tela isso
    elif idade > 70: #se tiver mais de 70 anos
        print("O senhor(a) está na idade onde é opcional votar ou não 👵!")
        #printando na tela isso
    elif idade <= 15: # Se for menor ou igual a 15
        faltam = - 16 - idade # Calcula os anos que faltam para a pessoa votar
        print(f"Você é menor de idade. Ainda faltam {faltam} ano(s) para votar\U0001F600.")
        #Opção para por qualquer frase na tela da pessoa com emoji \U0001F600.