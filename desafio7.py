#Exibe o título do programa
print("--- Calculadora de Juros Simples ---")
#Solicita o valor do capital inicial (dinheiro investido) e converte para float
capital = float(input("Digite o Capital inicial (R$): "))
#Solicita a taxa de juros em porcentagem (%) e converte para float
taxa = float(input("Digite a taxa de juros (em %): "))
#Solicita o tempo em meses e converte para float
tempo = float(input("Digite o tempo (número de meses): "))
#Calcula os juros simples usando a fórmula:
#juros = capital * (taxa/100) * tempo
juros = capital * (taxa / 100) * tempo
#Calcula o montante total (capital + juros)
montante = capital + juros
#Imprime uma linha separadora com 30 traços
print("-" * 30)
#Exibe o valor dos juros formatado com 2 casas decimais
print(f"Valor dos Juros: R$ {juros:.2f}")
#Exibe o montante total também com 2 casas decimais
print(f"Montante Total: R$ {montante:.2f}")
