ano_inicio = int(input())
ano_fim = int(input())

ano = ano_inicio
bissextos = 0

while ano <= ano_fim:
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(ano)
        bissextos += 1
    ano += 1

print("bissextos:", bissextos)
