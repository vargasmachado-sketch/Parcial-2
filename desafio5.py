#Solicita a base e a altura ao usuário
base = float(input("Digite o valor da base do triângulo: "))
altura = float(input("Digite o valor da altura do triângulo: "))
#Realiza o cálculo
area = (base * altura) / 2
#Exibe o resultado com duas casas decimais
print(f"A área do triângulo é: {area:.2f}")
