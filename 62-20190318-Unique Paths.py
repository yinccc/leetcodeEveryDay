uniqpath={}

def uniq(m,n):
    if (m,n) in uniqpath:
        return uniqpath[(m,n)]
    if m<1 or n<1:
        return 0
    if m==1 or n==1:
        return 1
    uniqpath[(m,n)]=uniq(m-1,n)+uniq(m,n-1)
    return uniqpath[(m,n)]


print(uniq(3,7))