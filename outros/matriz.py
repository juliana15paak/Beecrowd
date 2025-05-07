# Leitura da matriz original
matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para a linha {i + 1}, coluna {j + 1}: "))
        linha.append(valor)
    matriz.append(linha)

# Criando a matriz transposta
matriz_transposta = [[0 for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        matriz_transposta[j][i] = matriz[i][j]

# Exibindo a matriz transposta
for linha in matriz_transposta:
    for elemento in linha:
        print(elemento, end=" ")
    print()
