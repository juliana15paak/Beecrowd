num_casos = int(input())
divisor = 1
soma = 0
num = 0
while num_casos > 0:
    num = int(input())
    while divisor < num:
        if num % divisor == 0:
            soma += divisor
        divisor += 1
    num_casos -= 1
    if soma == num:
        print(num, "eh perfeito")
    else:
        print(num, "nao eh perfeito")
    divisor = 1
    soma = 0
    num = 0

