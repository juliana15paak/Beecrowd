num_participantes = int(input())
paises = []
for _ in range(num_participantes):
    pais, ouros, pratas, bronzes = input().split()
    ouros, pratas, bronzes = int(ouros), int(pratas), int(bronzes)
    paises.append([pais, ouros, pratas, bronzes])
paises.sort()
paises.sort(key = lambda item: item[3], reverse=True)
paises.sort(key = lambda item: item[2], reverse=True)
paises.sort(key = lambda item: item[1], reverse=True)
for pais, ouros, pratas, bronzes in paises:
    print(pais, ouros, pratas, bronzes)
