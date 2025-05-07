x = int(input())
y = int(input())

soma = 0

if x < y:
    i = x + 1  
    j = y - 1  
else:
    i = y + 1 
    j = x - 1  

while i <= j:
    if i % 2 != 0:
        soma += i
    i += 1  

print(soma)
