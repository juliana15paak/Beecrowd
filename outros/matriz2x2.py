# Criando uma matriz 2x2 com entrada do usuário
matriz = []

for i in range(2):
    linha = []
    for j in range(2):
        valor = int(input(f"Digite o valor para posição [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

# Exibindo a matriz
print("\nMatriz 2x2:")
for linha in matriz:
    print(linha)
