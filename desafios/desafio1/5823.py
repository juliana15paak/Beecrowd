preco = float(input())
tara = int(input())
alimento = float(input())

alimento = alimento * 1000

peso = alimento - tara

alimento = peso / 100

preco_total = alimento * preco
print(f"Total = R$ {preco_total:.2f}")


