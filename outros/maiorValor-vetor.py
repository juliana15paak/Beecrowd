# Leitura dos números e verificação do maior valor
numeros = [0] * 5
maior = numeros[0]

for i in range(len(numeros)):
    numeros[i] = int(input(f"Digite o {i + 1}º valor: "))
    if i == 0 or numeros[i] > maior:
        maior = numeros[i]

print("O maior valor é:", maior)
