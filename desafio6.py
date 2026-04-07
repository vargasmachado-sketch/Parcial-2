#Exibe o título do programa
print("--- Conversor de Tempo ---")
#Pergunta ao usuário qual tipo de conversão ele deseja fazer
opcao = input("Digite 1 para converter segundos → h/m/s ou 2 para converter h/m/s → segundos: ")
#Se o usuário escolher converter de segundos para horas/minutos/segundos
if opcao == "1":
    #Solicita o valor em segundos e converte para inteiro
    total_segundos = int(input("Digite o tempo em segundos: "))
    #Calcula quantas horas existem dentro do total de segundos
    horas = total_segundos // 3600
    #Calcula o restante após retirar as horas
    resto = total_segundos % 3600
    #Calcula os minutos a partir do restante
    minutos = resto // 60
   #Calcula os segundos finais que sobraram
    segundos = resto % 60
    #Exibe o resultado formatado
    print(f"{horas}h {minutos}m {segundos}s")
#Se o usuário escolher converter de horas/minutos/segundos para segundos
elif opcao == "2":
    #Solicita as horas, minutos e segundos separadamente
    horas = int(input("Digite as horas: "))
    minutos = int(input("Digite os minutos: "))
    segundos = int(input("Digite os segundos: "))
    #Converte tudo para segundos
    total_segundos = (horas * 3600) + (minutos * 60) + segundos
    #Exibe o resultado final
    print(f"Total em segundos: {total_segundos}")
#Caso o usuário digite uma opção inválida
else:
    print("Opção inválida.")
