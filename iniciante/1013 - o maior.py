a, b, c = input().split()
a, b, c = int(a), int(b), int(c)

MaiorAB = (a+b+abs(a-b))/2
if c > MaiorAB:
    maior = c
else:
    maior = MaiorAB
    
maior = int(maior)
print(maior, 'eh o maior')
