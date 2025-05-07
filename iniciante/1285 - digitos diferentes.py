while True:
    try:
        n, m = map(int, input().split())
        soma = 0
        while n <= m:
            n = str(n)
            if len(n) == 4:
                if n[0] != n[1] and n[0] != n[2] and n[0] != n[3] and n[1] != n[2] and n[1] != n[3] and n[2] != n[3]:
                    soma += 1
            elif len(n) == 3:
                if n[0] != n[1] and n[0] != n[2] and n[1] != n[2]:
                    soma += 1
            elif len(n) == 2:
                if n[0] != n[1]:
                    soma += 1
            elif len(n) == 1:
                soma += 1
            n = int(n)
            n += 1
        print(soma)
    except EOFError:
        break
