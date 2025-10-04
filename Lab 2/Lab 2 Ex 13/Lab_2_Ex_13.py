import math

indice = 0

def primMod(n):
    if(n<3):
        return 1
    if(n%2==0):
        return 0
    for i in range (3, int(math.sqrt(n))+1, 2):
        if (n%i==0):
            return 0
    return 1

def printDesc(numar, n):
    fact=2
    global indice
    while (numar>1):
        if(numar%fact==0):
            for i in range(fact):
                indice+=1
                if(indice==n):
                    print(fact)
                    #indice+=1
                    return
            while(numar%fact==0):
                numar//=fact
        fact+=1

n = int(input())
print(f"Elementul {n} al sirului este: ", end="")

numar=1
while(indice<n):
    if(primMod(numar)):
        indice+=1
        if(indice==n):
            print(numar)
    else:
        printDesc(numar, n)
    numar+=1


     


