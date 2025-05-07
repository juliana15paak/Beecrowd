idade = int(input())

ano = idade // 365
idade = idade - (ano * 365)
mes = idade // 30
idade = idade - (mes * 30)
dia = idade
idade = idade - (dia * 30)

print(f"{ano} ano(s)")
print(f"{mes} mes(es)")
print(f"{dia} dia(s)")
