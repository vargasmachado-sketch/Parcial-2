# Programa para calcular Juros Simples

print("--- Calculadora de Juros Simples ---")

capital = float(input("Digite o Capital inicial (R$): "))
taxa = float(input("Digite a taxa de juros (em %): "))
tempo = float(input("Digite o tempo (número de meses): "))

# Cálculo dos juros (i / 100 para converter a porcentagem em decimal)
juros = capital * (taxa / 100) * tempo

# Cálculo do montante final
montante = capital + juros

print("-" * 30)
print(f"Valor dos Juros: R$ {juros:.2f}")
print(f"Montante Total: R$ {montante:.2f}")
