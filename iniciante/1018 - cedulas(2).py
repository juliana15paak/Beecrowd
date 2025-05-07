money = int(input())

cedulas = [
    (100, "nota(s) de R$ 100,00"),
    (50, "nota(s) de R$ 50,00"),
    (20, "nota(s) de R$ 20,00"),
    (10, "nota(s) de R$ 10,00"),
    (5, "nota(s) de R$ 5,00"),
    (2, "nota(s) de R$ 2,00"),
    (1, "nota(s) de R$ 1,00"),
]

print(money)
for valor, label in cedulas:
    qtd_nota = money // valor
    money %= valor
    print(qtd_nota, label)
