#Pede ao usuário que digite um número inteiro e converte a entrada para tipo int
num = int(input("Digite um número inteiro: "))
#Verifica se o resto da divisão de 'num' por 2 é igual a 0, se sim, é par o número
if num % 2 == 0:
    #Exibe a mensagem noticiando número par
    print("O número é par.")
else:
    #Caso o resto da divisão não for 0 (ou seja 1), ele informa número ímpar
    print("O número é ímpar.")
