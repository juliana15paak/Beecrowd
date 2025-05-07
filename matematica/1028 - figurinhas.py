casos_teste = int(input())
while casos_teste > 0:
    f1, f2 = map(int, input().split())
    maior_figurinha = 0
    
    if f1 > f2:
        maior_figurinha = f1
    else:
        maior_figurinha = f2
        
    maior_pilha = 0
    i = 1
    while i <= maior_figurinha:
        if f1 % i == 0 and f2 % i == 0:
                maior_pilha = i
        i += 1
    print(maior_pilha)
    casos_teste -= 1
