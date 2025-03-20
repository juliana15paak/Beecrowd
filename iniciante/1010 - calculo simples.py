cod1, num_pecas1, valor_unitario1 = input().split()
cod1, num_pecas1, valor_unitario1 = int(cod1), int(num_pecas1), float(valor_unitario1)
cod2, num_pecas2, valor_unitario2 = input().split()
cod2, num_pecas2, valor_unitario2 = int(cod2), int(num_pecas2), float(valor_unitario2)
preco = num_pecas1 * valor_unitario1 + num_pecas2 * valor_unitario2
print(f"VALOR A PAGAR: R$ {preco:.2f}")
