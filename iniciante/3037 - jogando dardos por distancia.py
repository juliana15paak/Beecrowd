num_casos = int(input())

while num_casos > 0:
    i = 0
    pontuacaoJ = 0
    while i < 3:
        joaoX, joaoY = map(int, input().split())
        pontuacaoJ += joaoX*joaoY
        i += 1
    i = 0
    pontuacaoM = 0
    while i < 3:
        mariaX, mariaY = map(int, input().split())
        pontuacaoM += mariaX*mariaY
        i += 1
    num_casos -= 1
    if pontuacaoJ > pontuacaoM:
        print("JOAO")
    elif pontuacaoM > pontuacaoJ:
        print("MARIA")
