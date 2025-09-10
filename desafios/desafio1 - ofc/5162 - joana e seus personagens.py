dia, mes, ano = map(int, input().split('/'))

soma = dia + mes + ano

if soma % 2 == 0:
    print("par")
else:
    print("impar")
