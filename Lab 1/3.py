def cmmdc(a, b):
    
    if(a==b):
        return a
    if(a==0):
        return b
    if(b==0):
        return a
    else:
        if(a>b):
            return cmmdc(a-b, b)
        else:
            return cmmdc(a, b-a)

a = int(input())
b = int(input())
print(cmmdc(a, b))
