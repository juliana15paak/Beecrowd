money = round(float(input()), 2)
centavos = int(round(money * 100))

notas_moedas = [
    (10000, "nota", "R$ 100.00"),
    (5000,  "nota", "R$ 50.00"),
    (2000,  "nota", "R$ 20.00"),
    (1000,  "nota", "R$ 10.00"),
    (500,   "nota", "R$ 5.00"),
    (200,   "nota", "R$ 2.00"),
    (100,   "moeda", "R$ 1.00"),
    (50,    "moeda", "R$ 0.50"),
    (25,    "moeda", "R$ 0.25"),
    (10,    "moeda", "R$ 0.10"),
    (5,     "moeda", "R$ 0.05"),
    (1,     "moeda", "R$ 0.01")
]

print("NOTAS:")
for valor, tipo, label in notas_moedas:
    if tipo == "nota":
        qtd = centavos // valor
        centavos %= valor
        print(f"{qtd} nota(s) de {label}")

print("MOEDAS:")
for valor, tipo, label in notas_moedas:
    if tipo == "moeda":
        qtd = centavos // valor
        centavos %= valor
        print(f"{qtd} moeda(s) de {label}")
