nomes = []
for i in range(5):
    nome = input(f"Digite o nome {i+1}: ")
    nomes.append(nome)
print("Os nomes digitados foram:")
for nome in nomes:
    print(nome)
