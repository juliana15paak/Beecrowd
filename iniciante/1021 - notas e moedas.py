money = round(float(input()), 2)

nota100 = 0
nota50 = 0
nota20 = 0
nota10 = 0
nota5 = 0
nota2 = 0
moeda1 = 0
moeda050 = 0
moeda025 = 0
moeda10 = 0
moeda05 = 0
moeda01 = 0

centena = money // 100

if centena > 0:
    nota100 = centena
    centena = centena * 100
    money = round((money - centena), 2)
    
dezena = money % 100 // 10

if dezena >= 5:
    nota50 = 1
    dezena = dezena - 5
    money = round((money - 50), 2)

if dezena >= 2:
    nota20 = dezena // 2
    dezena = dezena * 10
    money = money - dezena
    dezena = round((money % 100 // 10), 2)

if dezena >= 1:
    nota10 = dezena // 1
    dezena = dezena * 10
    money = round((money - dezena), 2)

unidade = money % 10 // 1

if unidade >= 5:
    nota5 = 1
    unidade = unidade - 5
    money = round((money - 5), 2)

if unidade >= 2:
    nota2 = unidade // 2
    unidade = nota2 * 2
    money = round((money - unidade), 2)
    
unidade = money % 10 // 1

if unidade >= 1:
    moeda1 = unidade
    money = round((money - unidade), 2)

decimal = money * 100
decimal1 = decimal % 100 // 10

if decimal1 >= 5:
    moeda050 = 1
    decimal1 = decimal1 - 5
    decimal = decimal - 50

if decimal >= 25:
    moeda025 = decimal // 25
    decimal = decimal - 25
   
if decimal >= 10:
    moeda10 = decimal // 10
    decimal = decimal - (moeda10 * 10)

if decimal >= 5:
    moeda05 = decimal // 5
    decimal = decimal - (moeda05 * 5)
    
if decimal >= 1:
    moeda01 = decimal

nota100, nota50, nota20, nota10, nota5, nota2, moeda1, moeda050, moeda025, moeda10, moeda05, moeda01 = map(int, (nota100, nota50, nota20, nota10, nota5, nota2, moeda1, moeda050, moeda025, moeda10, moeda05, moeda01))

print("NOTAS:")
print(f"{nota100} nota(s) de R$ 100.00")
print(f"{nota50} nota(s) de R$ 50.00")
print(f"{nota20} nota(s) de R$ 20.00")
print(f"{nota10} nota(s) de R$ 10.00")
print(f"{nota5} nota(s) de R$ 5.00")
print(f"{nota2} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{moeda1} moeda(s) de R$ 1.00")
print(f"{moeda050} moeda(s) de R$ 0.50")
print(f"{moeda025} moeda(s) de R$ 0.25")
print(f"{moeda10} moeda(s) de R$ 0.10")
print(f"{moeda05} moeda(s) de R$ 0.05")
print(f"{moeda01} moeda(s) de R$ 0.01")
    


    
