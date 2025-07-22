def once(a):
    n=len(a)
    a.sort()
    print(a)
    for i in range(1,n-1):
        if a[i]!=a[i-1] and a[i]!=a[i+1]:
            print(a[i],end=" ")
    if a[n-1]!=a[n-2]:
        print(a[n-1],end="")

la=[2,5,6,2,7,11,8,5,6,8,9]
once(la)


def once_hash(a1):
    l=len(a1)
    maxi=max(a1)
    print(maxi)
    hash=[0]*(maxi+1)
    print("hash array is ",hash)

    for num in a1:
        hash[num] += 1
    
    for num in a1:
        if hash[num]==1:
            print(num)

list1=[3,7,8,2,4,6,4,7,8,3,2]
once_hash(list1)
