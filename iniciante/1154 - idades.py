i = 0
idade = 0
soma = 0

while idade >= 0:
    idade = int(input())
    soma += idade
    i += 1
    
media = soma / i
print(f"{media:.2f}")
