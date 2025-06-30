
a=[0,2,1,1,4,5,1,1,1,1,9]
n=len(a)
count=0
maxi=0

for i in range(n):
    if a[i]==1:
       count+=1
       maxi=max(count,maxi)
    else:
        count=0

print(maxi)
    


