c={}
def climbing(n):
    if n in c:
        return c[n]
    if n==1:
        return 1
    if n==2:
        return 2
    c[n]=climbing(n-1)+climbing(n-2)
    return c[n]


n=climbing(3)
print(n)
