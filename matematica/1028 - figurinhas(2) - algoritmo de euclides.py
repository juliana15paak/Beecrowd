casos_teste = int(input())

def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

while casos_teste > 0:
    f1, f2 = map(int, input().split())
    print(mdc(f1,f2))
    casos_teste -= 1
