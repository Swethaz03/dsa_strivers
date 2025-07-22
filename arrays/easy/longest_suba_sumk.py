
def subarray(a,k):
    l=len(a)
    res=0
    for i in range(0,l):
        sum=0
        for j in range(i,l):
            sum+=a[j]
            if sum==k:
                length=(j-i+1)
                res=max(res,length)
    print(res)

a1=[10,5,2,7,1,9]
subarray(a1,15)
