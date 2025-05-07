n = int(input())
i = 1
fatorial = n
if 0 < n and n < 13:
    while i < n:
        f = (n-i)
        fatorial = fatorial * f
        i += 1
print(fatorial)
