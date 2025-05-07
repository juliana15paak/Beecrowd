i = 1
maior = 0
posicao = 0
while i <= 100:
    x = int(input())
    if x > maior:
        maior = x
        posicao = i
    i += 1
print(maior)
print(posicao)
