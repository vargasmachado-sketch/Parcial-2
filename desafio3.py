#Cria uma lista vazia para armazenar os nomes digitados
nomes = []
#Inicia um laço que será executado 5 vezes (0 até 4)
for i in range(5):
    #Solicita ao usuário que digite um nome
    #O {i+1} serve para mostrar a contagem começando em 1 ao invés de 0
    nome = input(f"Digite o nome {i+1}: ")
    #Adiciona o número digitado na lista 'nomes'
    nomes.append(nome)
#Exibe uma mensagem antes de listar os nomes
print("Os nomes digitados são:")
#Percorre cada item (nome) dentro da lista 'nomes'
for nome in nomes:
#Imprime cada nomes com um hífen na frente
    print(f" - {nome}")

