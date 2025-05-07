x = int(input())
y = int(input())
 
if x > y:
    c = x
    x = y
    y = c
 
soma = 0
i = x + 1
if i % 2 == 0:
    i += 1
 
while i < y:
    soma += i
    i += 2
 
print(soma)
