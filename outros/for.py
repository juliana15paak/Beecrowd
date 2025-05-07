numero = int(input())

unidade = numero % 10
dezena = (numero % 100) // 10
centena = numero // 100

partes = []

if centena > 0:
    if centena == 1:
        partes.append("1 centena")
    else:
        partes.append(f"{centena} centenas")

if dezena > 0:
    if dezena == 1:
        partes.append("1 dezena")
    else:
        partes.append(f"{dezena} dezenas")

if unidade > 0:
    if unidade == 1:
        partes.append("1 unidade")
    else:
        partes.append(f"{unidade} unidades")

if len(partes) == 3:
    print(f"{partes[0]}, {partes[1]} e {partes[2]}")
elif len(partes) == 2:
    print(f"{partes[0]} e {partes[1]}")
elif len(partes) == 1:
    print(partes[0])
