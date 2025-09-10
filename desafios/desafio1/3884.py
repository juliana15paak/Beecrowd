inicio = int(input())
fim = int(input())
bissexto = 0

while inicio <= fim:
    if inicio % 4 == 0 and inicio % 100 != 0 or inicio % 400 == 0:
        print(inicio)
        bissexto += 1
    inicio += 1

print(f"bissextos: {bissexto}")
