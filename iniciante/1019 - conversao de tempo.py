tempo = int(input())

hora = tempo // (60 * 60)
tempo = tempo % (60 * 60)

minuto = tempo // 60
tempo = tempo % 60

segundo = tempo

print(f"{hora}:{minuto}:{segundo}")
