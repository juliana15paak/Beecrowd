from math import ceil, sqrt

ct = int(input())
while ct > 0:
    def primo(n):
        if n % 2 == 0: return n == 2
        raiz = ceil(sqrt(n))
        for pd in range(3, raiz+1, 2):
            if n % pd == 0:
                return False
        return True
        
    n = int(input())
    if primo(n) == True:
        print("Prime")
    else:
        print("Not Prime")
    ct -= 1
