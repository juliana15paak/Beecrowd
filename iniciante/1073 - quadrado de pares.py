N = int(input())
i = 1

if 5 < N and N < 2000:
    while i <= N:
        if i % 2 == 0:
            quadrado = i**2
            print(f"{i}^2 = {quadrado}")
        i += 1
