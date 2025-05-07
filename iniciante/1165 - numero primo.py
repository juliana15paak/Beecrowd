def primo(x):
  qtd_divisores = 0
  potencial_divisor = 1
  while potencial_divisor <= x:
      if x % potencial_divisor == 0:
          qtd_divisores += 1
      potencial_divisor += 1
  if qtd_divisores == 2:
      return True
  else:
    return False

quantos = int(input())
while quantos > 0:
    n = int(input())
    if primo(n):
        print(f"{n} eh primo")
    else:
        print(f"{n} nao eh primo")
    quantos -= 1
    




    
