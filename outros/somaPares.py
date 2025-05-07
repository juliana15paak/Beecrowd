# Soma de números pares com confirmação do usuário
i = 2
soma = 0
c = 1

while True:
    soma += i
    print("Soma:", soma)
    c = int(input("Gostaria de continuar?\nDigite 1 para sim ou 0 para não: "))
    i += 2
    if c != 1:
        break
