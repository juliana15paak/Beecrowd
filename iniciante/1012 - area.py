A, B, C = input().split()
A, B, C = float(A), float(B), float(C)

area_triangulo_retangulo = A * C / 2
area_circulo = 3.14159 * C**2
area_trapezio = (A + B)*C/2
area_quadrado = B**2
area_retangulo = A*B

print(f"TRIANGULO: {area_triangulo_retangulo:.3f}")
print(f"CIRCULO: {area_circulo:.3f}")
print(f"TRAPEZIO: {area_trapezio:.3f}")
print(f"QUADRADO: {area_quadrado:.3f}")
print(f"RETANGULO: {area_retangulo:.3f}")
