limite = int(input())
a, b = 0, 1
for _ in range(limite):
	print(a, end=' ')
	a, b = b, a + b
