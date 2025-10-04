import math

def prim (n):
    for i in range(2, int(math.sqrt(n))+1):
        if(n%i==0):
            return 0
    return 1

n = int(input())
if(prim(n)):
    print("este prim")
else:
    print("nu este prim")
    
