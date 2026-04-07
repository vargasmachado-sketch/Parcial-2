#Solicita ao usuário o primeiro número e converte para float (número decimal)
num1 = float(input("Digite o primeiro número: "))
#Solicita o segundo número e também converte para float
num2 = float(input("Digite o segundo número: "))
#Pergunta qual operação o usuário deseja realizar (+, -, * ou /)
operacao = input("Digite a operação (+, -, *, /): ")
#Verifica se a operação escolhida é soma
if operacao == "+":
    #Realiza a soma
    resultado = num1 + num2
#Verifica se a operação é subtração
elif operacao == "-":
    #Realiza a subtração
    resultado = num1 - num2
#Verifica se a operação é multiplicação
elif operacao == "*":
     #Realiza a multiplicação
    resultado = num1 * num2
#Verifica se a operação é divisão
elif operacao == "/":
    #Antes de dividir, verifica se o segundo número não é zero
    if num2 != 0:
         #Realiza a divisão
        resultado = num1 / num2
        #Caso o divisor seja zero, retorna uma mensagem de erro
    else:
        resultado = "Erro: divisão por zero"
        #Caso o usuário digite uma operação inválida
else:
    #Define uma mensagem de erro
    resultado = "Operação inválida"
    #Exibe o resultado final
print("Resultado:", resultado)
