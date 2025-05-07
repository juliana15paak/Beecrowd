casos_teste = int(input())
while casos_teste > 0:
    f1, f2 = map(int, input().split())
    
    if f1 > f2:
        i = f2
    else:
        i = f1
        
    maior_pilha = 0
    while i > 0:
        if f1 % i == 0 and f2 % i == 0:
                maior_pilha = i
                break
        i -= 1
    print(maior_pilha)
    casos_teste -= 1
