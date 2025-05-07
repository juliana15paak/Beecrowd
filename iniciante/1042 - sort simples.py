a, b, c = map(int, input().split())

primeiro = 0
segundo = 0
terceiro = 0

if a > b and b > c:
    primeiro = c
    segundo = b
    terceiro = a
elif a > c and c > b:
    primeiro = b
    segundo = c
    terceiro = a
elif b > a and a > c:
    primeiro = c
    segundo = a
    terceiro = b
elif b > c and c > a:
    primeiro = a
    segundo = c
    terceiro = b
elif c > a and a > b:
    primeiro = b
    segundo = a
    terceiro = c
elif c > b and b > a:
    primeiro = a
    segundo = b
    terceiro = c

print(primeiro)
print(segundo)
print(terceiro)

print(f"\n{a}")
print(b)
print(c)
