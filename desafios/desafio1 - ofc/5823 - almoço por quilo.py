preco_grama = float(input())
tara = int(input())
peso_prato = float(input())

peso_prato *= 1000
peso = peso_prato - tara
total = peso / 100 * preco_grama

print(f"Total = R$ {total:.2f}")
